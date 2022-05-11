string = input("Enter a string : ").lower()
unique_words = []
for i in range(len(string)):
    if string[i] not in unique_words:
        unique_words.append(string[i])
        
print("Unique words : ", end="")
for i in range(len(unique_words)):
    print(unique_words[i] , end=" ")
