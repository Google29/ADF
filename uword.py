one=[]
two=[]
try:
    outputFile=open("two.txt","w")
    try:
        inputFile=open("one.txt","r").read().split(' ')
        for i in inputFile:
            word=''
            for c in i:
                if(c!='\n'):
                    count=0
                    for v in i:
                        if(c==v):
                            count+=1
                    if(count==1):
                        word=word+c
            one.append(len(word))
            word=word+str(len(word))
            two.append(word)
        one.sort()
        for w in one:
            for x in two:
                if(w==int(x[len(x)-1])):
                    outputFile.write(x+' ')
                    two.remove(x)
                    break
        print('File transfer executed successfully')
        outputFile.close()
    except IOError:
        print('Unable to open source file')
except IOError:
    print('Unable to open destination file')