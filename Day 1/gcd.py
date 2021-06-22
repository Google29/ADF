def calculate_gcd(x,y):
    while(y):
        x,y=y,x%y
    return x
x=int(input('Enter the first value : '))
y=int(input('Enter the second value : '))
gcd=calculate_gcd(x,y)
print("The GCD is",gcd)