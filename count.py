def count_vowels_and_consonants(str):
    vowels = set("aeoiuAEIOU")
    num_vowels = 0
    num_consonants = 0

    for char in str: 
        if char.isalpha():
            if char in vowels:
                num_vowels += 1
            else:
                num_consonants += 1
        
    return num_vowels, num_consonants

str = input("ENTER THE STRING: ")
vowels, consonants = count_vowels_and_consonants(str)
print(f"Number of vowels: {vowels}\nNUmber Of consonants: {consonants}")