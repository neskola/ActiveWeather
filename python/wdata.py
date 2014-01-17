#!C:\Python33\python.exe -u
#!/usr/bin/env python

import sys, getopt
import urllib.request
import xml.etree.ElementTree as ET
import time
from datetime import datetime, timedelta

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

	# some static values
	api_key = "8a861995-5bad-4fea-85e8-7cccd6860bb2"
	query = "/wfs?request=getFeature&storedquery_id=fmi::forecast::hirlam::surface::point::timevaluepair&place="
	place = "porvoo"
	timestep = 60

	end_time = calculateEndtime()

	complete_query = "/fmi-apikey/" + api_key + query + place + "&timestep=" + str(timestep) + "&endtime" + end_time.strftime("%Y-%m-%dT%H:%S:%MZ")

	print(complete_query);

	if inputfile == '':	
		response = urllib.request.urlopen("http://data.fmi.fi" + complete_query)
		print (response.status, response.reason)
		xml = response.read()
		xml_root = ET.fromstring(xml)
	else:
		tree = ET.parse(inputfile)
		xml_root = tree.getroot()		
		
	print(xml_root)

def calculateEndtime():
	tmp_date = datetime.today()
	tmp_date = tmp_date + timedelta(hours=48)	
	return datetime(tmp_date.year, tmp_date.month, tmp_date.day, tmp_date.hour, 0,0)
	
if __name__ == "__main__":
	main(sys.argv[1:])