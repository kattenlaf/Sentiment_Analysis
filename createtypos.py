from difflib import SequenceMatcher

def similar(string_A, string_B):
  return SequenceMatcher(None, string_A, string_B).ratio()
  
#Need to create a function that generates typos

def substr(string):
    j=1
    a=set()
    while True:
        for i in range(len(string)-j+1):
            a.add(string[i:i+j])
        if j==len(string):
            break
        j+=1
        #string=string[1:]
    return a
    
def returnArrayOfStrings( mainString, typoString ):
  returnList = []
  mylist = substr(typoString)
  for string in mylist:
    #Two Typos
    if (similar(string,mainString) > 0.85 and abs((len(mainString) - len(string) <= 2))):
      #print string
      returnList.append(string)
  return returnList
  
finallist = []
finallist += returnArrayOfStrings("Cancerous", "Cancerousad")
finallist += returnArrayOfStrings("Cancerous", "Vancerousw")
print "Length of the list is", len(finallist)
for i in finallist:
  print i
    
