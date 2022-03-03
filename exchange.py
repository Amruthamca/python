def change_char(str1):
    char=str1[0]
    str1=str1.replace(char,'$')
    str1=char+str1[1:]
    return str1
a=input("Enter the string ")
print(change_char(a))
