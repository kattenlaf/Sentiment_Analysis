import textblob


positiveTweets = []
neutralTweets = []
negativeTweets = []

numberOfTweets = 0
myfile = open("myText.txt", "r") #Text file with the tweets we want

for line in myfile:
	numberOfTweets = numberOfTweets + 1
	analysis = textblob.TextBlob(line)

	if ( analysis.sentiment.polarity > 0 ):
		positiveTweets.append(analysis.sentiment.polarity)

	elif ( analysis.sentiment.polarity == 0 ):
		neutralTweets.append(analysis.sentiment.polarity)

	else:
		negativeTweets.append(analysis.sentiment.polarity)

print(positiveTweets)
print(neutralTweets)
print(negativeTweets)
sumTweets = len(positiveTweets) + len(negativeTweets) + len(neutralTweets)
print(sumTweets)
percentagePositive = len(positiveTweets)/sumTweets
percentageNeutral = len(neutralTweets)/sumTweets
percentageNegative = len(negativeTweets)/sumTweets
print(percentagePositive)
print(percentageNeutral)
print(percentageNegative)
myfile.close()