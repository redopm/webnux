#!/usr/bin/python2
import cgi
import cgitb
import commands
import mysql
import mysql.connector 

connection = mysql.connector.connect(host='localhost',database='mydb',user='root',passwd='admin')
cur = connection.cursor()
print "Content-type:text/html\r\n\r\n"
print ""

data=cgi.FieldStorage()

name = data.getvalue("uname")
print(user name)
print "<br/>"

email = data.getvalue("email")
print(email)
print "<br/>"

password = data.getvalue("psw")
print(password)
print "<br/>"

cur.execute("INSERT INTO user(user_name,email_id,password) VALUES(%s,%s,%s)", (user_name,email_id,password))
connection.commit()
#fetching  database
cur.execute("select *   from user")
print  cur.fetchall()
connection.close()
