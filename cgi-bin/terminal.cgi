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
mycmd=mypage.getvalue("in_cmd")

if mycmd :
	print "<html>"
	print "<meta http-equiv='refresh' content='3;url=http://localhost/terminal.html' />"
	print "<body style='background-color:powderblue;'>"
	print "<h1>>>>----------------------------> welcome to Webnux <---------------------------<<<</h1>"
	print "<hr style='color:red; border-width: 2px;'>"
	print "<h2>Your Expacted output :</h2>"
	print "<pre><h2>"
	print commands.getoutput("sudo "+mycmd)
	print "<pre></h2>"
	print "</body>"
	print "</html>"

else :
	redirectURL = "http://localhost/terminal.html"
	print('<html>')
	print('  <head>')
	print('    <meta http-equiv="refresh" content="0;url='+str(redirectURL)+'" />') 
	print('  </head>')
	print('</html>')


