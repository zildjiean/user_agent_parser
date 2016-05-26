#!/usr/python
import httpagentparser
import sys

#s = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36"

s = sys.argv[1]
agent = httpagentparser.detect(s)
platform = str(agent["platform"]["name"])
version = str(agent["platform"]["version"])
#bot = str(agent["bot"])
browser = str(agent["browser"]["name"])
bversion = str(agent["browser"]["version"])

print "Platform : "+platform+" |  "+" Version : "+version+" |  "+" Browser type : "+browser+" |  "+" Browser Version : "+bversion
