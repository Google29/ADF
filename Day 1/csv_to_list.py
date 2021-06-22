import csv

file=input('Enter the file name : ')
inputCSV=open(file,'r')
dict_list=[]
for line in csv.DictReader(inputCSV):
    dict_list.append(line)
print(dict_list)
