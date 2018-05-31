__author__ = 'Troy D. Anderson II'

def remover(sentence, blacklist):
    for i in blacklist:
        sentence = sentence.replace(i, ' ', len(sentence))
    return sentence

def removeAT(sentence):
    sentence += " "  # feeds without a space ending the string because code searches for one after each '@'
    while sentence.find("@") != -1:  # -1 is returns when substring is not found
        # find returns an to where substring is first located
        sentence = sentence.replace(sentence[sentence.find("@") : sentence.find(" ", sentence.find("@"))], "", 1)
    return sentence

def removelink(sentence,linktag):
    sentence = " " + sentence  # feeds without a space starting the string since code looks for a space before link
    for i in linktag:
        while sentence.find(i) != -1:
            # rfind() return the beginning of the word, so used len() method to offset range to end of word
            sentence = sentence.replace(sentence[sentence.rfind(" ", 0, sentence.rfind(i)+len(i)) : sentence.rfind(i)+len(i)],"",1)
    return sentence