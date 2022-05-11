def factorial(num):
    if num == 1:
        return num
    else:
        return num * factorial(num-1)
        
number = int(input("Enter a number : "))
fact = factorial(number)
print("Factorial is : ", fact)
