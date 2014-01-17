#!C:\Python33\python.exe -u
#!/usr/bin/env python

import sys, getopt
import urllib.request
import xml.etree.ElementTree as ET
import time
from datetime import datetime, timedelta

# namespaces
gml_namespace = "{http://www.opengis.net/gml/3.2}"
wml2_namespace = "{http://www.opengis.net/waterml/2.0}"

# some static values
api_key = "8a861995-5bad-4fea-85e8-7cccd6860bb2"
query = "/wfs?request=getFeature&storedquery_id=fmi::forecast::hirlam::surface::point::timevaluepair&place="
place = "porvoo"
timestep = 60


def main(argv):

	inputfile = ""
	try:
		opts, args = getopt.getopt(argv,"hf:", ["file="])
	except getopt.GetoptError:
		print ("wdata.py -file <xml_file>")
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print ("wdata.py -file <xml_file>")
			sys.exit()
		elif opt in ("-f", "--file"):
			inputfile = arg
	
	print (inputfile)		

	end_time = calculateEndtime()

	complete_query = "/fmi-apikey/" + api_key + query + place + "&timestep=" + str(timestep) + "&endtime" + end_time.strftime("%Y-%m-%dT%H:%S:%MZ")

	

	if inputfile == '':	
		print("Connecting to: " + complete_query);
		response = urllib.request.urlopen("http://data.fmi.fi" + complete_query)
		print (response.status, response.reason)
		xml = response.read()
		xml_root = ET.fromstring(xml)
	else:
		print("Reading xml file: " + inputfile)
		xml_root = ET.parse(inputfile)
				
		
	parseXMLtoJSON(xml_root)

def calculateEndtime():
	tmp_date = datetime.today()
	tmp_date = tmp_date + timedelta(hours=48)	
	return datetime(tmp_date.year, tmp_date.month, tmp_date.day, tmp_date.hour, 0,0)
	
def parseXMLtoJSON(xml_root):	
	beginPosition = xml_root.find('.//{0}beginPosition'.format(gml_namespace))
	endPosition = xml_root.find('.//{0}endPosition'.format(gml_namespace))
	print ("Report dates:" + beginPosition.text, "to " + endPosition.text)
	
	#print(xml_root.find(".//{0}MeasurementTimeseries[@id='mts-1-1-Temperature']".format(wml2_namespace))) doesn't work. again something wierd in syntax
	measurements = xml_root.findall(".//{0}MeasurementTimeseries".format(wml2_namespace))
	for measurement in measurements:		
		m_id = measurement.get('{0}id'.format(gml_namespace))		
		# list which values will be included in an array variable - or better one: make a json mapping
		if m_id == 'mts-1-1-Temperature':
			printMeasurementTVPs(measurement, "temperature   :")
		if m_id == 'mts-1-1-Humidity':
			printMeasurementTVPs(measurement, "humidity     %:")
		if m_id == 'mts-1-1-WindSpeedMS':
			printMeasurementTVPs(measurement, "wind spd   m/s:")
		if m_id == 'mts-1-1-WindDirection':
			printMeasurementTVPs(measurement, "wind direction:")
		if m_id == 'mts-1-1-TotalCloudCover':
			printMeasurementTVPs(measurement, "cloud cover  %:")
		if m_id == 'mts-1-1-PrecipitationAmount':
			printMeasurementTVPs(measurement, "precipitation :")
		
			
def printMeasurementTVPs(measurement, type):
	tvps = measurement.findall("./{0}point/{0}MeasurementTVP".format(wml2_namespace)) # TPV = time value pair						
	for tvp in tvps:
		time = tvp.find("./{0}time".format(wml2_namespace))
		value = tvp.find("./{0}value".format(wml2_namespace))
		print (type, time.text, value.text)
					
if __name__ == "__main__":
	main(sys.argv[1:])