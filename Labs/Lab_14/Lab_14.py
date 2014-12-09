## Problem 1:
#1. Create a count of how many total words appear in Green Eggs and Ham
def greenEggs():

 seus =["I am Sam I am Sam Sam I am That Sam I am That Sam I am I do not like that Sam I am"]

 for item in seus:
   print len(item.split())

 #if len(seus) != 0 :
  ##wordlist = list(word for line in seus for word in line.split(” “))
   #for words in uniquewords:
    #   print words.rstrip(‘\n’),” : “,wordlist.count(words),” occurence”

#2. Create a count of how often each of the words appears (note that Eggs eggs Eggs! eggs? and eggs, should all be counted as the same word).  
Print out the total count and the count for each of the words. 
def count_words(filename):

 f = open(filename,'r')
 words_dict={}
 for i in f.read().split():
   word=i.lower()
   words_dict[word]= words_dict.get(word,0) + 1
 for key in words_dict.keys():
   print str(key)+' = '+str(words_dict[key])

#3. Print out the total count and the count for each of the words. 



#4. Print out the most commonly occuring word in the book



## Problem 2:
#1. Use the tools in your web browser to 
        #A. View the source for the page (this is the html code that makes up the page)
        #B. Save the page as an html file on your local drive
#2. Then open the file in JES 
#3. Use string processing techniques to extract the headlines from the paper.
        #A. Hint, refer back to the string documentation if you need to: http://docs.python.org/2/library/string.html
        #B. Hint: Remember that if you use the read command you end up with the whole file as a string this means you can boil this problem down to identifying the substring in the file that contains the headline
