import sys
from collections import Counter

try:
    #iFile=sys.argv[1]
    iFile='Ass 2.txt'
    inputFileList=open(iFile,'r').read().split(' ')
    if(len(inputFileList)!=0):
        to=0
        ing=0
        palindrome=[]
        uniqueList=[]
        for word in inputFileList:
            if(word[:2]=='To' or word[:2]=='to'):
                to+=1
            if(word[-3:]=='ing'):
                ing+=1
            if(word.lower()==word[::-1].lower()):
                palindrome.append(word)
        print("Number of words whose prefix is To/to : ",to,'\n')
        print('Number of words whose suffix is "ing" : ',ing,'\n')
        dict=Counter(inputFileList)
        max=0
        for key in dict:
            if(dict[key]>max):
                max=dict[key]
        print('Word(s) with maximum number of occurance is : ',end=" ")
        fisrtWord=True
        for key in dict:
            uniqueList.append(key)
            if(fisrtWord and dict[key]==max):
                print(key,end="")
                fisrtWord=False
                continue
            if(dict[key]==max):
                print(','+key,end="")
        print('\n\nPalindrome word(s) : '+str(palindrome)[1:-1])
        print('\nUnique list : ',uniqueList)
        Word={}
        i=1
        for word in inputFileList:
            Word[i]=word
            i+=1
        print('\nDictionary : ',Word)
    else:
        print('The given file is empty')
except ValueError:
    print('Unable to open given file')