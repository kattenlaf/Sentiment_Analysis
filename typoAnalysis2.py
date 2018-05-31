# Clean the typos of \n and store

typo_file = open("typos.txt", "r")
cleaned_type_file = open("cleaned_typos.txt", "w")

for word in typo_file:
    word = word.replace('\\n', "").replace('\n', "").lower()
    cleaned_type_file.write(word)
    cleaned_type_file.write('\n')
    cleaned_type_file.flush()
cleaned_type_file.close()