#!/usr/bin/python
import  cgi
import  commands
import  os
import  cgitb  # traceback errors in  web apps
cgitb.enable()
print  "Content-Type: text/html\r\n\r\n"
print  ""
# gettting  html data 
mypage=cgi.FieldStorage()
#print mypage
#mycmd=mypage.getvalue('cmd')
#print mycmd
if 'install' in mypage:
	mycmd=mypage.getvalue('install')
	print "<html>"
	print "<meta http-equiv='refresh' content='10000;url=http://127.0.0.1/sortware.html' />"
	print "<body style='background-color:powderblue;'>"
	print "<h1>>>>----------------------------> welcome to Webnux <---------------------------<<<</h1>"
	print "<hr style='color:red; border-width: 2px;'>"
	print "<h2>Your Expacted output :</h2>"
	print "<pre><h2>"
	print os.system("sudo apt-get install "+mycmd+" -y")
	#print mycmd+ " Software are successfully Installed"
	print "<pre></h2>"
	print "</body>"
	print "</html>"
	exit()
elif 'remove' in mypage:
	mycmd=mypage.getvalue('remove')
	print "<html>"
	print "<meta http-equiv='refresh' content='10000;url=http://127.0.0.1/sortware.html' />"
	print "<body style='background-color:powderblue;'>"
	print "<h1>>>>----------------------------> welcome to Webnux <---------------------------<<<</h1>"
	print "<hr style='color:red; border-width: 2px;'>"
	print "<h2>Your Expacted output :</h2>"
	print "<pre><h2>"
	print os.system("sudo apt-get autoremove "+mycmd+" -y")
	print mycmd+ " Software are successfully Uninstalled"
	print "<pre></h2>"
	print "</body>"
	print "</html>"
elif 'start' in mypage :
	mycmd=mypage.getvalue('start')
	print "<html>"
	print "<meta http-equiv='refresh' content='3;url=http://127.0.0.1/sortware.html' />"
	print "<body style='background-color:powderblue;'>"
	print "<h1>>>>----------------------------> welcome to Webnux <---------------------------<<<</h1>"
	print "<hr style='color:red; border-width: 2px;'>"
	print "<h2>Your Expacted output :</h2>"
	print "<pre><h2>"
	print os.system("sudo systemctl restart "+mycmd)
	print mycmd+ " Software Service are Started"
	print "<pre></h2>"
	print "</body>"
	print "</html>"
elif 'stop' in  mypage :
	mycmd=mypage.getvalue('stop')
	print "<html>"
	print "<meta http-equiv='refresh' content='3;url=http://127.0.0.1/sortware.html' />"
	print "<body style='background-color:powderblue;'>"
	print "<h1>>>>----------------------------> welcome to Webnux <---------------------------<<<</h1>"
	print "<hr style='color:red; border-width: 2px;'>"
	print "<h2>Your Expacted output :</h2>"
	print "<pre><h2>"
	print os.system("sudo systemctl stop "+mycmd)
	print mycmd+ " Software Service are Stoped"
	print "<pre></h2>"
	print "</body>"
	print "</html>"
elif 'enable' in mypage :
	mycmd=mypage.getvalue('enable')
	print "<html>"
	print "<meta http-equiv='refresh' content='3;url=http://127.0.0.1/sortware.html' />"
	print "<body style='background-color:powderblue;'>"
	print "<h1>>>>----------------------------> welcome to Webnux <---------------------------<<<</h1>"
	print "<hr style='color:red; border-width: 2px;'>"
	print "<h2>Your Expacted output :</h2>"
	print "<pre><h2>"
	print os.system("sudo systemctl enable "+mycmd)
	print mycmd+ " Software Service are enabled"
	print "<pre></h2>"
	print "</body>"
	print "</html>"
elif 'check' in mypage:
	mycmd=mypage.getvalue('check')
	print "<html>"
	print "<meta http-equiv='refresh' content='120;url=http://127.0.0.1/sortware.html' />"
	print "<body style='background-color:powderblue;'>"
	print "<h1>>>>----------------------------> welcome to Webnux <---------------------------<<<</h1>"
	print "<hr style='color:red; border-width: 2px;'>"
	print "<h2>Your Expacted output :</h2>"
	print "<pre><h2>"
	print commands.getoutput("sudo dpkg -L "+mycmd)
	print mycmd+ " Software All list are here..."
	print "<pre></h2>"
	print "</body>"
	print "</html>"
else:
	print "<html>"
	print "<meta http-equiv='refresh' content='3;url=http://127.0.0.1/sortware.html' />"
	print "<body style='background-color:powderblue;'>"
	print "<h1>>>>----------------------------> welcome to Webnux <---------------------------<<<</h1>"
	print "<hr style='color:red; border-width: 2px;'>"
	print "<h2>Your Expacted output :</h2>"
	print "<pre><h2>"
	print "Please enter software name."
	print "<pre></h2>"
	print "</body>"
	print "</html>"
	

