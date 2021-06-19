def decimal_to_Hexa(num):
    hex = ''
    while (num != 0):
        if (num % 16 < 10):
            hex = str(num % 16) + hex
        else:
            hex = chr((num % 16) + 55) + hex
        num = int(num / 16)
    return hex


def decimal_to_Octal(num):
    oct = ''
    while (num != 0):
        oct = str(num % 8) + oct
        num = int(num / 8)
    return oct;


def decimal_to_Binary(num):
    ans=''
    while (num != 0):
        if (num % 2 == 0):
            ans='0'+ans
        else:
            ans='1'+ans
        num = int(num / 2)
    return ans


num=int(input('Enter the decimal number : '))

print('input = '+str(num)+'\n Binary Conversion : '+decimal_to_Binary(num)+'\n Octal Conversion : '+decimal_to_Octal(num)+'\n Hexa Conversion : '+decimal_to_Hexa(num))

