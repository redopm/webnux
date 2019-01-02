#!/usr/bin/python
import  cgi
import  commands
import  os
import  cgitb  # traceback errors in  web apps
cgitb.enable()

print  "Content-Type: text/html"
print  ""
# gettting  html data 
mypage_data=cgi.FieldStorage()
cmd=mypage_data.getvalue('in_cmd')
mycmd=mypage_data.getvalue('open Terminal')
if cmd:
	print "<-------Welcome to Webnux------> \n<------ Your terminal is Ready----->"
	print   "<br/>"
	print   "<pre>"
	print   commands.getoutput('sudo  '+cmd)
	print   "</pre>"
elif mycmd:
	print "<-------Welcome to Webnux------> \n<------ Your terminal is Ready----->"
	print "open terminal..."
else:
	print "Error"
	


