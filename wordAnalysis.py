from PyDictionary import PyDictionary

dictionary = PyDictionary()

known_words = set()

unknown_words = set()

cleaned_file = open("cleaned.txt", "r")

known_words_file = open("known_words.txt", "w")

unknown_words_file = open("unknown_words.txt", "w")

for sentence in cleaned_file:
    words = sentence.split()
    for word in words:
        meaning = dictionary.meaning(word)
        meaning = str(meaning)
        if ( meaning != "None"):

            if word not in known_words:
                known_words.add(word)
                known_words_file.write(word + "\n")
                known_words_file.flush()
        else:

            if ( word not in unknown_words and word not in known_words ):
                unknown_words.add(word)
                term = "Word : " + word
                unknown_words_file.write(word + "\n")
                unknown_words_file.flush()

cleaned_file.close()
known_words_file.close()
unknown_words_file.close()
