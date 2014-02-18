#!C:\Python33\python.exe -u
#!/usr/bin/env python

import sys, getopt, json
import curl
import xml.etree.ElementTree as ET
import time
import firebase
from datetime import datetime, timedelta

# namespaces
gml_namespace = "{http://www.opengis.net/gml/3.2}"
wml2_namespace = "{http://www.opengis.net/waterml/2.0}"
target_namespace = "{http://xml.fmi.fi/namespace/om/atmosphericfeatures/0.95}"

# some static values
api_key = "8a861995-5bad-4fea-85e8-7cccd6860bb2"
query = "/wfs?request=getFeature&storedquery_id=fmi::forecast::hirlam::surface::point::timevaluepair&place="
place = "Porvoo"
geoid = ''
timestep = 60

weather_table = dict()

def main(argv):
	global place, geoid
	
	inputfile = ""
	try:
		opts, args = getopt.getopt(argv,"hf:p:g:", ["file=", "place=", "geoid="])
	except getopt.GetoptError:
		print ("wdata.py -file <xml_file> -p <place>")
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print ("wdata.py -file <xml_file>")
			sys.exit()
		elif opt in ("-f", "--file"):			
			inputfile = arg
			print ("Using " + inputfile + " as input file.")
		elif opt in ("-p", "--place"):			
			place = arg
			print ("Using " + place + " as place parameter.")
		elif opt in ("-g", "--geoid"):
			goeid = arg
			print ("Using " + geoid + " as geoid parameter.")
	
	end_time = calculateEndtime()

	complete_query = "/fmi-apikey/" + api_key + query + place + "&timestep=" + str(timestep) + "&endtime" + end_time.strftime("%Y-%m-%dT%H:%S:%MZ")

	if inputfile == '':	
		print("Connecting to: " + complete_query);
		xml = firebase.curlQuery("http://data.fmi.fi" + complete_query)
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
	global place
	
	beginPosition = xml_root.find('.//{0}beginPosition'.format(gml_namespace))
	endPosition = xml_root.find('.//{0}endPosition'.format(gml_namespace))
	geoid = xml_root.find('.//{0}identifier'.format(gml_namespace))
	gmlpos = xml_root.find('.//{0}pos'.format(gml_namespace))
	timezone = xml_root.find('.//{0}timezone'.format(target_namespace))
	country = xml_root.find('.//{0}country'.format(target_namespace))
	region = xml_root.find('.//{0}region'.format(target_namespace))
	print ("Report dates:" + beginPosition.text, "to " + endPosition.text)
	print ("Place: " + place, " geoid: " + geoid.text, " gml pos: " + gmlpos.text)
	
	#print(xml_root.find(".//{0}MeasurementTimeseries[@id='mts-1-1-Temperature']".format(wml2_namespace))) doesn't work. again something wierd in syntax
	measurements = xml_root.findall(".//{0}MeasurementTimeseries".format(wml2_namespace))
	for measurement in measurements:		
		m_id = measurement.get('{0}id'.format(gml_namespace))		
		# list which values will be included in an array variable - or better one: make a json mapping
		if m_id == 'mts-1-1-Temperature':
			printMeasurementTVPs(measurement, "temp")
		if m_id == 'mts-1-1-Humidity':
			printMeasurementTVPs(measurement, "humi")
		if m_id == 'mts-1-1-WindSpeedMS':
			printMeasurementTVPs(measurement, "wspd")
		if m_id == 'mts-1-1-WindDirection':
			printMeasurementTVPs(measurement, "wdir")
		if m_id == 'mts-1-1-TotalCloudCover':
			printMeasurementTVPs(measurement, "ccvr")
		if m_id == 'mts-1-1-PrecipitationAmount':
			printMeasurementTVPs(measurement, "prct")
				
	root = dict()
	root['place'] = place
	root['geoid'] = geoid.text
	root['gml_pos'] = gmlpos.text
	root['timezone'] = timezone.text
	root['region'] = region.text
	root['country'] = country.text
		
	dictlist = []
		
	for value in sorted(weather_table.items()):		
		key = value[0]
		#print(key)
		dictlist.append(weather_table.get(key))
	
	root['data'] = dictlist;
	
	with open(place + '.json', 'w') as outfile:
		json.dump(root, outfile, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False)
	outfile.close()

	firebase.curlPut("https://activeweather.firebaseIO.com/observations/observation/" + geoid.text + ".json", json.dumps(root))	
	
	#print (json_data, file = place + '.json') # pretty print json	
	
def printMeasurementTVPs(measurement, type):	
	tvps = measurement.findall("./{0}point/{0}MeasurementTVP".format(wml2_namespace)) # TPV = time value pair						
	for tvp in tvps:
		time = tvp.find("./{0}time".format(wml2_namespace))
		value = tvp.find("./{0}value".format(wml2_namespace))
		#print (type, time.text, value.text)
		if time.text in weather_table:
			value_table = weather_table[time.text]						
			value_table[type] = value.text
		else:			
			value_table = dict()
			value_table[type] = value.text
			value_table['date'] = time.text			
			weather_table[time.text] = value_table		
	
if __name__ == "__main__":
	main(sys.argv[1:])
