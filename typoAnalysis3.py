from nltk.corpus import words
from time import sleep

typos = open('cleaned_typos.txt', 'r')
new_typos = open('new_typo.txt', 'w')
typo_count = {}
for word in typos:
    word = word.rstrip()
    if word not in typo_count:
        typo_count[word] = 1
    else:
        typo_count[word] = typo_count[word] + 1

word_list = words.words()

for word in typo_count:
    if word not in word_list:
        new_typos.write(word)
        new_typos.write('\n')
        new_typos.flush()
typos.close()
new_typos.close()