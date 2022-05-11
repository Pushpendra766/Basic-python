lst1 = []
print("Enter list elements : ", end="")
for i in range(0, 5):
    ele = input()
    lst1.append(ele)

lst2 = []
for i, j in zip(range(0, len(lst1)), range(len(lst1)-1, -1, -1)):
    lst2.append(lst1[j])
   
print("New list elements ", end="")   
for i in range(0, len(lst2)):
    print(lst2[i], end=" ") 
    
