lines = [['It', 'was', 'the', 'movie', '[noun]', 'come', 'to', 'life.',1],
['Sixteen', '[noun],', 'fourteen', 'passengers', 'and', 'two', 'crew', 'members', '[adverb]', 'began',2],
['[adverb]', 'on', 'a', '[noun]', 'from', '[noun]', 'to', 'Philadelphia', 'on', 'Friday,',3],
['forcing', 'the', 'pilot', 'to', 'make', 'an', 'emergency', 'stop', '[pronoun]', '[noun].',2],
['Various', 'news', 'reports', 'identified', 'a', '[noun]', 'in', 'the', 'cabin', 'which', 'caused', 'the', 'domino', 'effect', 'of', '[noun].',2],
['The', 'afflicted', 'passengers', 'were', 'rushed', 'to', 'the', 'closest', '[noun].',1],
['The', '[noun]', 'passengers', 'suffered', 'from', 'both', 'from', '[noun]', 'and', '[noun].',3],
['The', 'cause', 'of', 'the', '[noun]', 'remains', 'under', 'investigation.',1]]

test = ['Aliens', 'people', 'suddenly', 'screaming', 'space flight', 'mars', 'on', 'the moon', 'exomorph', 'panic', 'airlock', 'other', 'trauma', 'panic']
userWords = [''] * 14
lines2 = []

def madLibs():
  j = 0
  for data in lines:
    i = 0
    lastIndex = len(data) - 1
    pString = (data[:(lastIndex)])
    numWords = data[lastIndex]
    while(i < numWords and j < 14):
      sentence = ' '.join(pString)
      printNow(sentence)
      for word in pString:
        if(word.startswith('[')):
          askString = 'Enter a ' + word
          userInput = requestString(askString)
          userWords[j] = userInput
          j = j + 1
        i = i + 1

def madLibsMake():
  j = 0
  for data in lines:
    i = 0
    lastIndex = len(data) - 1
    pString = data[:lastIndex]
    numWords = data[lastIndex]
    while(i < (lastIndex - 1) and j < 14):
      for word in pString:
        if(word.startswith('[')):
           pString[i] = userWords[j]
           j = j + 1
        i = i + 1
    lines2.append(pString)
  printIt(lines2)
 
def printIt(theLines):
  for phrase in lines2:
   toPrint = ' '.join(phrase)
   printNow(toPrint)
