a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))
if a>b and a>c:
    print(a, "is largest.")
elif b>a and b>c:
    print(b, "is largest.")
elif c>a and c>b:
    print(c, "is largest.")    
