#!/usr/bin/env python

import httplib
import sys
import json

if len(sys.argv) !=4:
        print "Usage: %s '@user|#channel' subject message" % ( sys.argv[0], )
        sys.exit(1)

channel = sys.argv[1]
subject = sys.argv[2]
message = sys.argv[3]

if subject.startswith("Error"):
    emoji = ":crying_cat_face:"
    user = "Zabbix Alert"
    color = "danger"
else:
    emoji = ":smiley_cat:"
    user = "Zabbix Recovery"
    color = "good"

payload = {
  "channel": channel,
  "username": user,
  "icon_emoji": emoji,
  "attachments":[
      {
         "fallback": subject + ": " + message,
         "pretext": subject,
         "color": color,
         "text": message
      }
   ]  
}

conn = httplib.HTTPSConnection("yourcompany.slack.com", 443, timeout=10)
conn.request("POST", "/services/hooks/incoming-webhook?token=yourtoken",
  json.dumps(payload), 
  { "Content-type": "application/json" }
)
conn.getresponse()
