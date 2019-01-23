#!/usr/bin/python2
import tweepy
import sys
topic=sys.argv[1]
# define cosumer key and consumer secrete  
con_key=''
con_sec=''
# find authentication from authhandler from twitter by cosumer key and consumer secrete
auth=tweepy.OAuthHandler(con_key,con_sec)

# defind access key and secrete key 
acc_key=''
sec_key=''
#finally find the tocken to access database from authhandler 
auth.set_access_token(acc_key,sec_key)
conn=tweepy.API(auth)# we are connect to api

tweet=conn.search(topic)
for i in tweet:
	if 'html' in dir(tweet):
		print i 
	print i.text





