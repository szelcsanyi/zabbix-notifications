#!/usr/bin/env python

import httplib, urllib
import sys

if len(sys.argv) !=4:
        print "Usage: %s user subject message" % ( sys.argv[0], )
        sys.exit(1)

user = sys.argv[1]
subject = sys.argv[2]
message = sys.argv[3]

conn = httplib.HTTPSConnection("api.pushover.net:443")
conn.request("POST", "/1/messages.json",
  urllib.urlencode({
    "token": "yourtoken",
    "user": user,
    "message": message,
    "title": subject
  }), { "Content-type": "application/x-www-form-urlencoded" })
conn.getresponse()

