#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Copyright 2008 Juha Autero
#
# Copyright 2010 Juha Autero <jautero@iki.fi>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

project="Mobile Locator"
version="1.0"
author="Juha Autero <jautero@iki.fi>"
copyright="Copyright 2009, 2010 Pasi Takala, Jussi Kallio, Juha Autero"
application="mobilelocator"
import wsgiref.handlers
import os

from google.appengine.ext.webapp import template
from google.appengine.ext import webapp
from location import Location
from django.utils import simplejson
import logging

class SkiingBuddyFinder(webapp.RequestHandler):

    def get(self):
        template_values=globals()
        positions={}
        modifications={}
        for loc in Location.all():
            try:
                data=simplejson.loads(loc.position)
            except Exception, e:
                data=loc.position
            if not positions.has_key(loc.nick) or loc.modified>modifications[loc.nick]:
                positions[loc.nick]=data
                modifications[loc.nick]=loc.modified
        template_values["positions"]=simplejson.dumps(positions)
        template_values["sensor"]="false" # Don't use sensor yet.
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, template_values))
    
    def post(self):
        locnick=self.request.get('nick')
        if not locnick:
            return self.error("Parameter 'nick' missing")
        loc=Location(nick=locnick)
        loc.position=self.request.get('position')
        loc.put()
        return self.success()
    
    def success(self):
        self.response.out.write("STATUS=Success\n")
    
    def error(self,message):
        self.response.out.write("STATUS=Error\nerror_msg=%s" % (message))

def main():
    application = webapp.WSGIApplication([('/', SkiingBuddyFinder)],debug=True)
    wsgiref.handlers.CGIHandler().run(application)


if __name__ == '__main__':
    main()
