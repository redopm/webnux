#!/usr/bin/python2
import  urllib2
import  googlesearch  
#
a=raw_input("Search here... :")
webdata=googlesearch.search(a,num=1)
f=open('link.txt','w+')# open a file link.text and it exist then create write mod
for  i  in   webdata:
	print  i
	f.write("%s\n" %i) # this is the write operation in file
	f1=f.readline()
	for x in  f1:
		link=urllib2.urlopen(x)
		soup =googlesearch.BeautifulSoup(link, 'lxml')
		text = soup.get_text()
		print soup.text.encode('utf8')

	
