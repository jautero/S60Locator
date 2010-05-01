#!/usr/bin/env python
# encoding: utf-8
"""
location.py

Created by Juha Autero on 2010-05-01.
Copyright (c) 2010 Juha Autero. All rights reserved.
"""

import sys
import os
import unittest
from google.appengine.ext import db
class Location(db.Model):
    nick=db.StringProperty(required=True)
    position=db.TextProperty()
    modified=db.DateTimeProperty(auto_now=True)
#    user=db.UserProperty()

class buddyTests(unittest.TestCase):
	def setUp(self):
		pass


if __name__ == '__main__':
	unittest.main()