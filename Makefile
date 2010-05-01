gae-server/static_files/client.zip: client/simplejson.py client/gaeclient.py client/mobilelocator.py
	zip -j $@ $^
