'''
def reverse(str):
    str = list(str)
    i, j = 0, len(str) - 1

    while i < j:
        str[i], str[j] = str[j], str[i]
        i+=1
        j-=1
    return ''.join(str)
'''
def reverse(str):
    rev_str = ''
    for i in range(len(str)-1, -1, -1):
        rev_str += str[i]
    return rev_str

str = input("ENTER THE STRING: ")
print("ORIGINAL STRING: {0} \nREVERSED STRING: {1}".format(str, reverse(str)))