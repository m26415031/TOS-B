#!/usr/bin/python

import re
import string

f=open('/etc/passwd','r')
this = re.sub(r'(\w+):(\w+):(\w+):(\w+):(([\w,\s]+)?):([\w\/]+):([\w\/]+)',r'\5',f.read())
this=re.sub(r'(\w+),([\w,]+)','\1',this)
print this.title()
