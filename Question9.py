st = input("Enter a string : ")
length = len(st)
vowel_count = 0
for i in range(0, length):
    if st[i] == 'a' or st[i] == 'e' or st[i] == 'i' or st[i] == 'o' or st[i] == 'u':
        vowel_count += 1
        
print("Number of vowels is", vowel_count)        
