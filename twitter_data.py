#!/usr/bin/python2
import tweepy
import sys
topic=sys.argv[1]
# define cosumer key and consumer secrete  
con_key='66QJ2YeU92hpV0meNTKByXgHf'
con_sec='wdnMsIyj28ACAJgdoab8U0TCodrCddWynCHGhURysqMbJTolvG'
# find authentication from authhandler from twitter by cosumer key and consumer secrete
auth=tweepy.OAuthHandler(con_key,con_sec)

# defind access key and secrete key 
acc_key='895958544603729920-V3o2mVu9rXDOkBkL1Rjy2o1x32lsp4L'
sec_key='UBBYUrgTISjPSde4mdCkEJGQdhIqFCW35Lh6hoqCrKLHH'
#finally find the tocken to access database from authhandler 
auth.set_access_token(acc_key,sec_key)
conn=tweepy.API(auth)# we are connect to api

tweet=conn.search(topic)
for i in tweet:
	if 'html' in dir(tweet):
		print i 
	print i.text





