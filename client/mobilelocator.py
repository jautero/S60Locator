#!/usr/bin/env python
# encoding: utf-8
"""
s60client.py

S60 Client for Skiing Buddy Finder.

Created by Juha Autero on 2010-01-17.
Copyright (c) 2010 Juha Autero. All rights reserved.
"""

# Hack to get simplejson to path
import sys
sys.path.append("e:\\data\\python\\sbf_modules")
import gaeclient
import appuifw, positioning

poll_interval=60000000

def main():
	gaeclient.name=appuifw.query(u"Your nick",'text')
	positioning.position(callback=gaeclient.positioning_callback,interval=poll_interval)

if __name__ == '__main__':
	main()

