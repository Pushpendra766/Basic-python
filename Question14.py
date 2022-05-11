def prime(num):
    for i in range(2, num):
        if(num % i == 0):
            return False
    return True        
        
number = int(input("Enter a number : "))
flag = prime(number)
if flag:
    print("It is prime.")
else:
    print("It is not prime")
