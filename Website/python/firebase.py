#!C:\Python33\python.exe -u
#!/usr/bin/env python
import sys, getopt, json, ssl
import curl

# for testing only
def main(): 
	getBatchControllerData("activeweather.firebaseIO.com");
	
# Firebase API functions, no fancy realtime stuff just plain PUSH / GET functions

# get batch controller data, such as places, timevalues etc for update batch jobs
def getBatchControllerData(firebase_url):
	print ("Using curl")
# push parsed json data to firebase
#def pushJSONtoFirebase(json, firebase_url):

if __name__ == "__main__":
	main()