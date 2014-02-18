#!C:\Python33\python.exe -u
#!/usr/bin/env python
import sys, getopt, json, ssl
import pycurl
import StringIO

# for testing only
def main(): 

	str = { "this is a test" }

	print getBatchControllerData("https://activeweather.firebaseIO.com");
	print getProfileData("https://activeweather.firebaseIO.com");

	curlPut("https://activeweather.firebaseIO.com/test", str)

# Firebase API functions, no fancy realtime stuff just plain PUSH / GET functions

# get batch controller data, such as places, timevalues etc for update batch jobs
def getBatchControllerData(firebase_url):
	return curlQuery(firebase_url + "/observations.json")

def getProfileData(firebase_url):
	return curlQuery(firebase_url + "/profiles.json")

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
	b = StringIO.StringIO(data)

	c = pycurl.Curl();
	c.setopt(pycurl.URL, url)
	c.setopt(pycurl.HTTPHEADER, ["Accept:"])
	c.setopt(pycurl.HTTPPOST, data)
	c.setopt(pycurl.CUSTOMREQUEST, "PUT")
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
