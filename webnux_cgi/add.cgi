#!/usr/bin/python
import  cgi
import  commands
import  os
import  cgitb  # traceback errors in  web apps
cgitb.enable()

print  "Content-Type: text/html "
print  ""
# gettting  html data 
mypage_data=cgi.FieldStorage()
mycmd=mypage_data.getvalue('in_cmd')

#  adding numbers 
print   "<br/>"
print   "<pre>"
print   commands.getoutput('sudo  '+mycmd)
print   "</pre>"


