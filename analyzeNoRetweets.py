myfile = open("noRetweets.txt", "r")
myNewFile = open("finalFile.txt", "w")
for tweet in myfile:
    #Replacing all the b' because of encoding
    if (tweet[0:2] == "b'"):
        tweet = tweet.replace("b'", "")
    elif (tweet[0:2] == 'b"'):
        tweet = tweet.replace('b"', "")
    if (tweet.endswith("'\n")):
        tweet = tweet[:-2] #Removes last character
    print(tweet)
    myNewFile.write(tweet)
    myNewFile.write("\n")
