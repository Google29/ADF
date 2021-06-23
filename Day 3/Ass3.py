import sys
import re
import logging
from collections import Counter
class newfile1:

    def __init__(self, f):
        self.f = f

    def one(self):
        try:
            name1 = open(self.f, 'r').read().split(' ')
            logging.debug(f'{self.f} file opened')
            return name1
        except FileNotFoundError:
            logging.debug('The file is unable to open'.format(self.f))

    def two(self):
        try:
            name2 = open(self.f, 'a')
            logging.debug(f'{self.f} file opened')
            return name2
        except FileNotFoundError:
            logging.debug('The file is unable to open'.format(self.f))

    def closeFile(self, file):
        file.close()

    def printDetails(self):
        pass


class newfile2(newfile1):

    def __init__(self, file):
        super(newfile2, self).__init__(file)

    def printDetails(self, t):
        print(t)

    def to(self, l1):
        to = 0
        for w in l1:
            if (w[:2] == 'to'):
                to += 1
        self.printDetails(to)

    def ing(self, l1):
        ing = 0
        for w in l1:
            if (w[-3:] == 'ing'):
                ing += 1
        self.printDetails(ing)

    def max(self, l1):
        dict = Counter(l1)
        ans = []
        max = 0
        for key in dict:
            if (dict[key] > max):
                max = dict[key]
        for key in dict:
            if (dict[key] == max):
                ans.append(key)
        self.printDetails(ans)

    def palindrome(self, l1):
        palindrome = []
        for w in l1:
            if (w.lower() == w[::-1].lower()):
                palindrome.append(w)
        self.printDetails(palindrome)

    def Uni(self, l1):
        dict = Counter(l1)
        u = []
        for key in dict:
            u.append(key)
        self.printDetails(u)

    def dict(self, l1):
        word = {}
        i = 1
        for w in l1:
            word[i] = w
            i += 1
        self.printDetails(word)

    def vowel(self, f, w):
        value = re.split('a|e|i|o|u', w)
        for vow in value:
            f.write(vow + ' ')

    def thirdltCap(self, g, w):
        try:
            g.write(w[:2] + w[2].upper() + w[3:])
        except IndexError:
            g.write(w)

logging.basicConfig(filename='word.log', level=logging.DEBUG, format='%(asctime)s:%(message)s')
file = 'Ass3.txt'
obj = newfile2(file)
name1 = obj.one()
if (len(name1) != 0):
    print(f'Number of words having prefix with “To” : ', end="")
    obj.to(name1)
    logging.debug('Count of words whose prefix "To" is determined')
    print('Number of words ending with “ing” : ', end="")
    obj.ing(name1)
    logging.debug('Count of words whose suffix "ing" is determined')
    print('Word that was repeated maximum number of times : ', end="")
    obj.max(name1)
    logging.debug('Words with maximum occurance is determined')
    print('Palindrome present in the file : ', end="")
    obj.palindrome(name1)
    logging.debug('Palindrome words is determined')
    print('Unique List : ', end="")
    obj.Uni(name1)
    logging.debug('Unique list is identified')
    print('Counter Index : ', end="")
    obj.dict(name1)
    logging.debug('Counter index dictionary is identified')

    file = 'folder'
    for i in range(4):
        fileObj = newfile2(file + str(i + 1) + '.txt')
        o = fileObj.two()
        s = -1
        for w in name1:
            s += 1
            if (i == 0):
                fileObj.vowel(o, w)
            elif (i == 1):
                fileObj.thirdltCap(o, w)
            elif (i == 2):
                if (s == 4):
                    o.write(w.upper() + ' ')
                    continue
                o.write(w)
            elif (i == 3):
                if (s == 0):
                    o.write(w)
                    continue
                else:
                    o.write('-' + w)
                    continue
            o.write(' ')
        if (i == 0):
            logging.debug('Writing splitted words based on vowels in a new file is completed')
        elif (i == 1):
            logging.debug('Converting the third letter of each word and write it in a new file is completed')
        elif (i == 2):
            logging.debug('Converting the fourth word of file and write it in a new file is completed')
        elif (i == 3):
            logging.debug('Converting the " " to "-" is done and write it in a new file is completed')
        fileObj.closeFile(o)
        logging.debug('{} file closed'.format(file + str(i + 1) + '.txt'))
    logging.debug('All operations are running successfully\n')

else:
    print('The File is Empty')
    logging.debug(f'The file {file} is empty')
