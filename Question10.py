string = input("Enter a string : ")
length = len(string)

first_letter = string[0]
middle_string = string[1:length-1]
last_letter = string[length-1]
new_string = last_letter + middle_string + first_letter

print(new_string)
