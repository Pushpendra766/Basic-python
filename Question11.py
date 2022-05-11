lst = []
print("Enter list elements")
for i in range(0, 7):
    ele = input()
    lst.append(ele)

print("Alternate elements")
for i in range(0, len(lst)):
    if(i % 2 == 0):
        print(lst[i], end=" ")
