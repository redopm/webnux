#!/usr/bin/python
import mysql.connector as mariadb
import cgi,cgitb
cgitb.enable()

print 'Content-Type:text/html, charset=utf-8;'
print ''
print 'hello world'

mariadb_connection = mariadb.connect(user='root', passwd='admin', database='mydb' hostname='localhost')
cursor = mariadb_connection.cursor()

#retrieving information
'''cursor.execute("SELECT first_name,last_name FROM employees WHERE first_name=%s", (some_name,))

for first_name, last_name in cursor:
    print("First name: {}, Last name: {}").format(first_name,last_name)

#insert information
try:
    cursor.execute("INSERT INTO employees (first_name,last_name) VALUES (%s,%s)", ('Maria','DB'))
except mariadb.Error as error:
    print("Error: {}".format(error))

mariadb_connection.commit()
print "The last inserted id was: ", cursor.lastrowid'''
cursor.execute('TRUNCATE user')
cursor.execute('INSERT INTO user value(1,'omprakash','opmaury2gmail.com',1/1/2019,'123456')')
cuesor.commit()
cursor.execute('SELECT * FROM user')
print cursor.fetchall()
#mariadb_connection.close()
