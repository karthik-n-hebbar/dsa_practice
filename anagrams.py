def anagrams(str1, str2):
    str1 = "".join(filter(str.isalpha, str1,)).lower()
    str2 = "".join(filter(str.isalpha, str2,)).lower()

    str1 = sorted(str1)
    str2 = sorted(str2)
    
    return str1 == str2

str1 = input("ENTER THE FIRST WORD: ")
str2 = input("ENTER THE FIRST WORD: ")

if anagrams(str1, str2):
    print("ANAGRAMS")
else:
    print("NOT A ANAGRAMS")

