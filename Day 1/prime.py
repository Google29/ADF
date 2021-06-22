from time import sleep,time
num=int(input('Enter the maximum range = '))
list=[True]*num
for i in range(2,num):
    if((i*i)<num and list[i]==True):
        for j in range(i*i,num,i):
            list[j]=False
for i in range(2,num):
    if(list[i]==True):
        print(i)
        sleep(5-time()%1)