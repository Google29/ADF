one=[]
two=[]
try:
    outputFile=open("two.txt","w")
    try:
        inputFile=open("one.txt","r").read().split(' ')
        for i in inputFile:

            if (inputFile.count(i) > 1):
                continue
            else:
                one.append(len(i))
                i = i + str(len(i))
                two.append(i)
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