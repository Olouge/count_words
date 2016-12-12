def searchnswapmax(wordArray,wordcountArray,n):
    # Hold current max word
    maxword = ""
    
    # Hold current max word count
    curwordcount = 0
    
    # Hold max word count
    maxwordcount = 0
    
    # Hold current word
    curword = ""
    
    # Temporal variables for swap
    tempword = ""
    tempcount = 0        
    if n > len(wordcountArray):
        n = len(wordcountArray)        
    for index in range(0,len(wordcountArray)-1):  
        #print("Iteration: ",index)
        #print("============================")
        if index < n:
            maxwordcount = wordcountArray[index]
            maxword = wordArray[index]    
            
            curwordcount = wordcountArray[index+1]
            curword = wordArray[index+1]
            for iindex in range(index+1,len(wordcountArray)-1):
                #print("Index: ",index)
                #print("IIndex: ",iindex)
                #print("Comparing: ",curword, " && ", maxword)
                #print("Positions: ",iindex, " && ", index)
                #print("Counts: ",curwordcount, " && ", maxwordcount)
                #print("")                
                if (curwordcount>maxwordcount):
                    tempcount = maxwordcount
                    tempword = maxword
                    
                    maxwordcount = curwordcount
                    maxword = curword
                    
                    curwordcount = tempcount
                    curword = tempword
                    
                    wordcountArray[index] = maxwordcount
                    wordArray[index] = maxword 
                    
                    wordcountArray[iindex] = curwordcount
                    wordArray[iindex] = curword  
                elif curwordcount == maxwordcount:
                    if (curword < maxword):
                        tempcount = maxwordcount
                        tempword = maxword
                        
                        maxwordcount = curwordcount
                        maxword = curword
                        
                        curwordcount = tempcount
                        curword = tempword
                        
                        wordcountArray[index] = maxwordcount
                        wordArray[index] = maxword 
                        wordcountArray[iindex] = tempcount
                        wordArray[iindex] = tempword
                    elif(curword == maxword):
                        iindex = iindex+1
                        curwordcount = wordcountArray[iindex]
                        curword = wordArray[iindex]
                else:
                    curwordcount = wordcountArray[iindex]
                    curword = wordArray[iindex]
                curwordcount = wordcountArray[iindex+1]
                curword = wordArray[iindex+1]    
        else:
            break
        
        #print(wordcountArray)
        #print("Length:", len(wordcountArray))
        #print("")
        #print(wordArray)
        #print("Length:", len(wordArray))
        #print("")
        #print("End Iteration: ",index)
        #index = index +1
    return    
    
def printSorted(wordArray,wordcountArray,n):
    tup = (0,0)
    newwords = []
    if n > len(wordcountArray):
        n = len(wordcountArray)
    for index in range(0,n):
        if index < n:
            tup = (wordArray[index],wordcountArray[index])
            newwords.append(tup)
    wordcountArray = []
    wordArray = []
    return newwords

def count_words(string,n):
    count1 = 0;    
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    not_punctuated = ""
    # Array to hold their count
    wordcountArray = []
    # Array to hold words
    wordArray = []
    
    # Remove punctuations
    for char in string:
        if char not in punctuations:
            not_punctuated = not_punctuated + char
    
    # Break down string into words        
    words = not_punctuated.split(" ");
    
    # Sort the list
    words.sort();
    #print(words)
    #print("")
    for word in words:
        if word not in wordArray:
            wordcountArray.append(words.count(word))
            wordArray.append(word)                                       
            count1 = count1 + 1
    #print(wordcountArray)
    #print("Length:", len(wordcountArray))
    #print("")
    #print(wordArray)
    #print("Length:", len(wordArray))
    #print("")
    searchnswapmax(wordArray,wordcountArray,n)
    return printSorted(wordArray,wordcountArray,n)
    
def test_run():
#    string = "betty bought a bit of butter but the butter was bitter"
    #raw_input("""Test count_words() with some inputs:""")
#    num = 3
    #input("Enter number of words for analysis:")    
    #print count_words(string, num)
    print count_words("cat bat mat cat bat cat", 3)
    print count_words("betty bought a bit of butter but the butter was bitter", 4)
    #print count_words("betty bought a bit of butter but the butter was bitter", 3)  

if __name__ == '__main__':
    test_run()    
#print count_words(user_input,n)
