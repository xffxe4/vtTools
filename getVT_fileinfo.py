#!/usr/bin/python
#
# Fetch file information of a hash from VT database and print pretty.
# bravobingomazinga@gmail.com
#

import sys
import simplejson as json
import urllib
import urllib2

APIKEY = "YOUR_APIKEY_HERE"

malhash = sys.argv[1]
url = "http://api.vtapi.net/vtapi/get_file_infos.json"
parameters = {"resources": malhash,"apikey":APIKEY}
data = urllib.urlencode(parameters)
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
json_data = response.read()
print json.dumps(json.loads(json_data), sort_keys=True, indent=4)
