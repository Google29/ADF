''' File '''
from collections import Counter
import re
try:
    FILE='ass4.txt'
    filelist=open(FILE,'r').read().split(' ')
    if len(filelist)!=0:
        TO=0
        for w in filelist:
            if w[:2]=='to':
                TO+=1
        print("Number of words having prefix with “To” : ", TO,'\n\n')

        ING = 0
        for w in filelist:
            if w[-3:]=='ing':
                ING+=1
        print('Number of words ending with “ing” : ', ING)



        palindrome = []
        for w in filelist:
            if w.lower() == w[::-1].lower():
                palindrome.append(w)
        print('\n\nPalindrome presented in the file : ', palindrome,'\n')
        Di = Counter(filelist)
        MAX = 0
        for k in Di:
            if Di[k] > MAX:
                MAX = Di[k]
        print('Words that was repeated maximum number of times : ',end=" ")

        maxList=[]
        uniqueList = []
        for k in Di:
            uniqueList.append(k)
            if Di[k]==MAX:
                maxList.append(k)
        print(maxList)

        print('\n\nUnique list presented in the file : ',uniqueList)
        Word={}
        i=1
        for w in filelist:
            Word[i]=w
            i+=1
        print('\nDictionary : ',Word)
        FILE = 'day2'
        for i in range(5):
            with open(FILE+str(i+1)+'.txt','a') as openFile:
                j = -1
                for w in filelist:  #pylint: disable=no-else-continue
                    j += 1
                    if i == 0:
                        value = re.split('a|e|i|o|u', w)
                        for letter in value:
                            openFile.write(letter + ' ')
                    elif i == 1:
                        try:
                            openFile.write(w[:2] + w[2].upper() + w[3:])
                        except IndexError:
                            openFile.write(w)
                    elif i == 2:
                        if j == 4:
                            openFile.write(w.upper() + ' ')
                            continue
                        openFile.write(w)
                    elif i == 3:
                        if j == 0:
                            openFile.write(w)
                            continue
                    else:
                        openFile.write('-' + w)
                        continue
                    openFile.write(' ')
                #openFile.close()
    else:
        print('The given file is empty')


except ValueError:
    print('The file is unable to open')
