#!/usr/bin/python2
import  googlesearch
from urllib2 import urlopen
a=raw_input("Enter your data:")
# all the link are store in the variable 
link=googlesearch.search(a,num=3, stop=2, pause=1)
for i in link:
	f=open('link.txt','w+')# open a file link.text and it exist then create write mod
	f.write("%s\n" %i) # this is the write operation in file
	f1=f.readlines() # this is read operation in file
	for x in f1:
		print x
		html=urlopen(x)
		soup =googlesearch.BeautifulSoup(html, 'lxml')
		text = soup.get_text()
		print soup.text.encode('utf8')
	f.close()
