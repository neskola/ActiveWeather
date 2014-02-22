#!C:\Python33\python.exe -u
#!/usr/bin/env python
import sys, getopt, json, ssl
import pycurl
import StringIO

# for testing only
def main(): 

#	json = '{ "text" : "this is a test - another python test" }'

	print getGEOIDList()
#	print getProfileData("https://activeweather.firebaseIO.com");

#	curlPut("https://activeweather.firebaseIO.com/test.json", json)

	print "\n"

# Firebase API functions, no fancy realtime stuff just plain PUSH / GET functions

# get batch controller data, such as places, timevalues etc for update batch jobs
def getBatchControllerData(firebase_url):
	return curlQuery(firebase_url + "/observations/observation.json")

def getProfileData(firebase_url):
	return curlQuery(firebase_url + "/profiles.json")

def getGEOIDList():
	datalist = json.loads(getBatchControllerData("https://activeweather.firebaseIO.com"))
	geoidlist = []
	for data in datalist:
		geoidlist.append(data)
	return geoidlist

def curlQuery(url):
	
	b = StringIO.StringIO()

	print "Using curl. Query=" + url
	c = pycurl.Curl();
	c.setopt(pycurl.URL, url)
	c.setopt(pycurl.HTTPHEADER, ["Accept:"])
	c.setopt(pycurl.WRITEFUNCTION, b.write)
	c.setopt(pycurl.VERBOSE, 1)
	c.setopt(pycurl.SSL_VERIFYPEER, 0)   
	c.setopt(pycurl.SSL_VERIFYHOST, 0)
	c.perform()
	
	ret = b.getvalue()
	b.close()
	return ret

def curlPut(url, data):

	c = pycurl.Curl();
	c.setopt(pycurl.URL, url)
	c.setopt(pycurl.HTTPHEADER, ["Accept:application/json"])
	c.setopt(pycurl.CUSTOMREQUEST, "PUT")
	c.setopt(pycurl.POSTFIELDS, data)
	c.setopt(pycurl.SSL_VERIFYPEER, 0)   
	c.setopt(pycurl.SSL_VERIFYHOST, 0)
	c.perform()

def curlDelete(url):

	c = pycurl.Curl();
	c.setopt(pycurl.URL, url)
	c.setopt(pycurl.HTTPHEADER, ["Accept:application/json"])
	c.setopt(pycurl.CUSTOMREQUEST, "DELETE")
#	c.setopt(pycurl.POSTFIELDS, data)
	c.setopt(pycurl.SSL_VERIFYPEER, 0)   
	c.setopt(pycurl.SSL_VERIFYHOST, 0)
	c.perform()


#def curlPost(url):

#def curlDelete(url):

def setupCurl():
	c = pycurl.Curl();
	c.setopt(pycurl.HTTPHEADER, ["Accept:"])
	c.setopt(pycurl.VERBOSE, 1)
	c.setopt(pycurl.SSL_VERIFYPEER, 0)   
	c.setopt(pycurl.SSL_VERIFYHOST, 0)


# push parsed json data to firebase
#def pushJSONtoFirebase(json, firebase_url):

if __name__ == "__main__":
	main()
