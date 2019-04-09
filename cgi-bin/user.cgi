#!/usr/bin/python
import  cgi, cgitb  # traceback errors in  web apps
import  commands
import  os
cgitb.enable()

print  "Content-Type: text/html"
print  ""
# gettting  html data 

mypage_data=cgi.FieldStorage()

if 'add' in mypage_data:
	mycmd=mypage_data.getvalue('add')
	print "<html>"
	print "<meta http-equiv='refresh' content='5;url=http://localhost/user.html' />"
	print "<body style='background-color:powderblue;'>"
	print "<h1>>>>----------------------------> welcome to Webnux <---------------------------<<<</h1>"
	print "<hr style='color:red; border-width: 2px;'>"
	print "<h2>Your Expacted output :</h2>"
	print "<pre><h2>"
	print commands.getoutput('sudo useradd '+mycmd)
	print mycmd+ " User are successfully Add. Thank you for  using our servive "
	print "<pre></h2>"
	print "</body>"
	print "</html>"
elif 'del' in mypage_data:
	mycmd=mypage_data.getvalue('del')
	print "<html>"
	print "<meta http-equiv='refresh' content='5;url=http://localhost/user.html' />"
	print "<body style='background-color:powderblue;'>"
	print "<h1>>>>----------------------------> welcome to Webnux <---------------------------<<<</h1>"
	print "<hr style='color:red; border-width: 2px;'>"
	print "<h2>Your Expacted output :</h2>"
	print "<pre><h2>"
	print commands.getoutput('sudo userdel '+mycmd)
	print mycmd+ " User are successfully Delete.  Thank you for  using our servive "
	print "<pre></h2>"
	print "</body>"
	print "</html>"
elif 'bash' in mypage_data:
	mycmd=mypage_data.getvalue('bash')
	print "<html>"
	print "<meta http-equiv='refresh' content='5;url=http://localhost/user.html' />"
	print "<body style='background-color:powderblue;'>"
	print "<h1>>>>----------------------------> welcome to Webnux <---------------------------<<<</h1>"
	print "<hr style='color:red; border-width: 2px;'>"
	print "<h2>Your Expacted output :</h2>"
	print "<pre><h2>"
	print commands.getoutput("sudo usermod --shell /bin/bash "+mycmd)
	print mycmd+ " /bin/bash are successfully Add."
	print "<pre></h2>"
	print "</body>"
	print "</html>"
elif 'nologin' in mypage_data:
	mycmd=mypage_data.getvalue('nologin')
	print "<html>"
	print "<meta http-equiv='refresh' content='5;url=http://localhost/user.html' />"
	print "<body style='background-color:powderblue;'>"
	print "<h1>>>>----------------------------> welcome to Webnux <---------------------------<<<</h1>"
	print "<hr style='color:red; border-width: 2px;'>"
	print "<h2>Your Expacted output :</h2>"
	print "<pre><h2>"
	print commands.getoutput("sudo usermod --shell /bin/nogin "+mycmd)
	print mycmd+ " /bin/bash are successfully Add."
	print "<pre></h2>"
	print "</body>"
	print "</html>"
	
else:
	print "you don't have root permission"

