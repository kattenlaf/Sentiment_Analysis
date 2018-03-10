import data as data
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time

consumer_key = 'ZWXZ5yeixFdDWNkdNyk9ugNKq'
consumer_secret = '8x3SbOD5CvybTSWCzLxJ4jAK4JxwkMCsZ4qJpmwb7q0Elu8LSe'
access_token = '812361304640000000-PwUtZe0JkdNW0DMt00JFh612SnKCJ2O'
access_secret = 'y5CS3IPhXjsbqIppQeX3EcMSOE8fK0yfoAQX05J87TZ2c'

class Listener( StreamListener ):

    def on_data( self, data ):
        try:
            tweet = data
            print tweet
            saveFile = open('Test.csv', 'a')
            saveFile.write(tweet)
            saveFile.write('\n')
            saveFile.close()
            #mydata
            tweet2 = data.split(',"text":"')[1].split('","source')[0]
            saveThis = str( time.time() ) + '::' + tweet
            saveFile2 = open('ruelFile.csv', 'a')
            saveFile2.write(saveThis)
            saveFile2.write('\n')
            saveFile2.close()
            return True
        except BaseException, e:
            print 'failed ondata,',str(e)
            time.sleep(10)

	def on_error(self, status):
		print status

auth = OAuthHandler( consumer_key, consumer_secret )
auth.set_access_token( access_token, access_secret )
keywords = [ "Nintendo", "Ninteno", "intendo", "Nintedo", "Nintendoi", "Nintend", "Niintendo" "iintendo"]
twitterStream = Stream( auth, Listener() )
twitterStream.filter(track=keywords)

#Stream tweets using the keyword in python2
