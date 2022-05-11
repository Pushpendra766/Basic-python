num = input("Enter a number : ")
length = len(num)
summation = 0
for i in range(0, length):
    summation += int(num[i])
print("Sum of digits is : ", summation)    
