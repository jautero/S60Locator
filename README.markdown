S60Locator
==========

Python code for running location service in S60 phone and on Google App Engine.

Basically the idea is that you run a python client in your phone that reports your position at intervals to the server.

API
===

/session?user=<user>

Start new session for user. Returns key to use in update. Not implemented yet.

/update?nick=nick&position=<position>

Send position information to server. 