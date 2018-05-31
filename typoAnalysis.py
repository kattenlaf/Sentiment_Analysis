from nltk.corpus import words

word_list = words.words()
typo_list = open("unknown_words.txt", "r")
cleaned_typo_list = open("typos.txt", "w")

for word in typo_list:
    word = word.rstrip()
    if word not in word_list:
        cleaned_typo_list.write(word)
        cleaned_typo_list.write("\n")
        cleaned_typo_list.flush()
cleaned_typo_list.close()