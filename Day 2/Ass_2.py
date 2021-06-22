from collections import Counter

try:
    file='Ass 2.txt'
    filelist=open(file,'r').read().split(' ')
    if(len(filelist)!=0):
        to=0
        for w in filelist:
            if(w[:2]=='to'):
                to+=1
        print("Number of words having prefix with “To” : ", to,'\n\n')

        ing = 0
        for w in filelist:
            if(w[-3:]=='ing'):
                ing+=1
        print('Number of words ending with “ing” : ', ing)



        palindrome = []
        for w in filelist:
            if (w.lower() == w[::-1].lower()):
                palindrome.append(w)
        print('\n\nPalindrome presented in the file : ' + str(palindrome)[1:-1],'\n')
        Di = Counter(filelist)
        max = 0
        for k in Di:
            if (Di[k] > max):
                max = Di[k]
        fisrtWord = True
        print('Words that was repeated maximum number of times : ',end=" ")

        uniqueList = []
        for k in Di:
            uniqueList.append(k)
            if(fisrtWord and Di[k]==max):
                print(k,end="")
                fisrtWord=False
                continue
            if(Di[k]==max):
                print(','+k,end="")

        print('\n\nUnique list presented in the file : ',uniqueList)
        Word={}
        i=1
        for w in filelist:
            Word[i]=w
            i+=1
        print('\nDictionary : ',Word)
    else:
        print('The given file is empty')
except ValueError:
    print('Unable to open given file')