lines = [['[Capitalized noun]', 'and', '[noun]', 'components have been', '[past-tense verb]', 'to the east', '[noun]', 'of North Korea in the last few days, a', '[noun]', 'with direct', '[plural noun]', 'of the information told', '[noun]', 'Thursday.',7],
['The', '[adjective]', '[noun]', 'comes amid further', '[adjective]', 'statements by North Korea and heightened', '[plural noun]', 'in the region -- a situation that /"does not need to get', '[adjective]', '/" a', '[noun]', 'said.',6],
['The', '[noun]', 'of the', '[noun]', 'and', '[noun]', 'equipment could mean that Pyongyang which unleashed another round of', '[adjective]', '[noun]', 'accusing', '[noun]', 'of pushing the region to the brink of', '[noun],', 'may be planning a', '[noun]', 'launch soon.',8],
['The components, the', '[noun]', 'said, are consistent with those of a', '[noun],', 'which has a', '[adjective]', 'range, meaning it could', '[verb]', '[noun],', '[noun],', 'and', '[noun].',7],
['[Capital Noun]', 'has been looking for a hidden North Korean east coast', '[noun]', 'or mobile', '[plural noun],', 'a', '[noun]', 'because a', '[noun]', 'from the east coast would go over Japan, the', '[noun]', 'said.',6],
['It is believed a', '[noun]', 'launch would be a test', '[noun]', 'rather than a', '[adjective]', '[noun]','. That is because it appears the North Koreans have only', '[pasttense verb]', 'the components so far.', '[Capitalized noun]', 'is waiting to see whether North Korea issues a', '[noun]', 'to its', '[plural noun]', 'and', '[plural noun]', 'to', '[verb]', 'the region.',10],
['Communication', '[plural noun]', 'in recent', '[plural noun]', 'also seem to show that Pyongyang might be planning to launch a mobile', '[noun]', 'in the', '[adjective]', 'days or weeks,', 'another', '[noun]', 'said.',5],
['Earlier,', '[noun]', 'told a', '[adjective]', 'committee in', '[Capitalized noun]', 'that the North has moved a', '[noun]', 'to its east coast for an', '[adjective]', 'test', '[noun]', 'or', '[noun]','.',7]]

test = ['Missile', 'launch', 'moved', 'coast', 'U.S. official', 'knowledge', 'CNN', 'apparent', 'deployment', 'threatening', 'tensions', 'hotter', 'U.S. State Department spokeswoman', 'move', 'missile', 'launch',  'scathing', 'rhetoric', 'the United States', 'war', 'missle', 'official', 'Musudan missile', '2,500-mile', 'threaten', 'South Korea', 'Japan', 'Southeast Asia', 'The United States', 'launch site', 'launchers', 'concern', 'launch', 'official', 'missile', 'launch', 'targeted', 'strike', 'moved', 'The United States', 'notice', 'airmen', 'mariners', 'stay out of', 'intercepts', 'days', 'ballistic missile', 'coming', 'U.S. official', 'South Korean Defense Minister Kim Kwan-jin', 'parliamentary', 'Seoul', 'medium-range missile', 'imminent', 'firing', 'military drill']
userWords = [''] * 56
lines2 = []

def madLibs():
  j = 0
  for data in lines:
    i = 0
    lastIndex = len(data) - 1
    pString = (data[:(lastIndex)])
    numWords = data[lastIndex]
    while(i < numWords and j < 56):
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
    while(i < (lastIndex - 1) and j < 56):
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