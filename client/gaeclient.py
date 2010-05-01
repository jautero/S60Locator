#!/usr/bin/env python
# encoding: utf-8
"""
gaeclient.py

Created by Juha Autero on 2010-01-18.
Copyright (c) 2010 Juha Autero. All rights reserved.
"""

import urllib,urllib2
import simplejson
import math, time

name="foobar"
api_url="http://mobilelocator.appspot.com/"
update_interval=60 # in seconds

previous_update=time.time()

def default_report(message):
  print message

report_callback=default_report

def update_position(name,position):
  """POST to Google App Engine webapp to update position."""
  params={"nick":name,"position":position}
  result={}
  paramstring=urllib.urlencode(params)
  for line in urllib2.urlopen(api_url,paramstring).readlines():
    if line.find("=")==-1:
      print line
    else:
      item=line.split("=",1)
      result[item[0].strip()]=item[1].strip()
  return result

def distance(point1,point2):
  lat1=math.radians(point1["latitude"])
  lat2=math.radians(point2["latitude"])
  lng1=math.radians(point1["longitude"])
  lng2=math.radians(point2["longitude"])
  return math.acos(math.sin(lat1)*math.sin(lat2) + math.cos(lat1)*math.cos(lat2) * math.cos(lng2-lng1)) * 6371000

def is_inside(person,place):
  return distance(person,place) < person["radius"]+place["radius"]
    
def positioning_callback(event):
  global previous_update
  if time.time() >= previous_update + update_interval:
    previous_update=time.time()
    data=server.update_position(buddy,simplejson.dumps(event["position"]))
 
def main():
	pass

if __name__ == '__main__':
	main()

