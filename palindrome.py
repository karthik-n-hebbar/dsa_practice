def is_palindrome(s):
    normalized_str = s.lower()
    rev_str = normalized_str[::-1]
    
    return normalized_str == rev_str

s = input("ENTER THE STRING: ")
if is_palindrome(s):
    print("IT IS A PALINDROME")
else:
    print("IT IS NOT A PALINDROME")