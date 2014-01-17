#!C:\Python33\python.exe -u
#!/usr/bin/env python

import urllib.request
import time
from datetime import datetime, timedelta

def calculateEndtime():
	tmp_date = datetime.today()
	tmp_date = tmp_date + timedelta(hours=48)	
	return datetime(tmp_date.year, tmp_date.month, tmp_date.day, tmp_date.hour, 0,0)

# some static values
api_key = "8a861995-5bad-4fea-85e8-7cccd6860bb2"
query = "/wfs?request=getFeature&storedquery_id=fmi::forecast::hirlam::surface::point::timevaluepair&place="
place = "porvoo"
timestep = 60

end_time = calculateEndtime()

complete_query = "/fmi-apikey/" + api_key + query + place + "&timestep=" + str(timestep) + "&endtime" + end_time.strftime("%Y-%m-%dT%H:%S:%MZ")

print(complete_query);

response = urllib.request.urlopen("http://data.fmi.fi" + complete_query)
print (response.status, response.reason)
xml = response.read()
print (xml)
	
