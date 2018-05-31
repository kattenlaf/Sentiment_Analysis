import troy as tr
import time

__author__ = 'Ruel Gordon'

#-----------------BLACK LISTS------------------#
punctuations = {'!', '.', ';', ':', '~', '#', '"', "'", '$', '/t', '/', '&', "\"", '\n', '-', ',', '(', ')', "\n", "?"}
linktag = {".com",".org",".java", "https", "co/", "co"}
#-----------------BLACK LISTS------------------#

#Write to files after tweets have been cleaned

mydictionary = {}
tweets = open('finalFile.txt', 'r')
cleanUp = open('cleaned.txt', 'w')

for _ in tweets:
    _ = tr.removeAT( _ )
    _ = tr.remover( _, punctuations )
    _ = tr.removelink( _, linktag )
    cleanUp.write(_)
    list = _.split()

    for word in list:
        if word in mydictionary:
            mydictionary[word] += 1
        else:
            mydictionary[word] = 1