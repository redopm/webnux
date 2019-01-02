#!/usr/bin/python
import  cgi
import  commands
import  os
import  cgitb  # traceback errors in  web apps
cgitb.enable()

print  "Content-Type: text/html "
print  ""
# gettting  html data 
mypage=cgi.FieldStorage()
#print mypage
mycmd=mypage.getvalue('cmd')

#print form
print "####----> Welcome to webnux---->####"
print   ""
print   "<br/>"
print   "<br/>"
print   "Your Outout is Displayed---->"
print   "<br/>"
print   ""
print   "<pre>"
print   commands.getoutput("sudo "+mycmd)
print   "</pre>"

# collect radio button
'''
if "cmd" :
#	command=mypage_data.getvalue('cmd')
	print "<h2>nothing entered!.</h2>"

else:
	cmd = form["cmd"].value
	print "choosed".format(cmd)
	print commands.getoutput('sudo  '+cmd)
	 
'''

