#!/usr/bin/env python

import httplib
import sys
import json

"""
Zabbix config for action (for default and recovery message):
Subject: {TRIGGER.STATUS} {TRIGGER.NSEVERITY}
Message: {HOST.NAME} ({HOST.IP}) {TRIGGER.NAME} ({ITEM.LASTVALUE})
"""

if len(sys.argv) !=4:
        print "Usage: %s group subject message" % ( sys.argv[0], )
        sys.exit(1)

group   = sys.argv[1]
subject = sys.argv[2]
message = sys.argv[3]

info = subject.split()

if info[0] == "OK":
    errortype = "recovery"
else:
    errortype = "error"

severity = info[1]

payload = {
  "group": group,
  "type": errortype,
  "message": message,
  "severity": severity
}

conn = httplib.HTTPSConnection("yourdomain", 443, timeout=10)
conn.request("POST", "/send",
  json.dumps(payload), 
  { "Content-type": "application/json" }
)
conn.getresponse()

