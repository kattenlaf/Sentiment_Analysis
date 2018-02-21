from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time

consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

class listener( StreamListener ):

	def on_data( self, data ):

		try:
			tweet = data.split(',"text":"')[1].split('","source')[0]
			print tweet
			saveThis = str( time.time() ) + '::' + tweet
			saveFile = open('Test.csv', 'a')
			saveFile.write(saveThis)
			saveFile.write('\n')
			saveFile.close()
			return True

		except BaseException, e:
			print 'failed ondata,',str(e)
			time.sleep(10)

	def on_error(self, status):
		print status

auth = OAuthHandler( consumer_key, consumer_secret )
auth.set_access_token( access_token, access_secret )

twitterStream = Stream( auth, listener() )
twitterStream.filter(track=["phone"])

#Stream tweets using the keyword in python2
