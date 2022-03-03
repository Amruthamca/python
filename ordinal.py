list=[]
a=input("enter a word")
n=len(a)
print("letters in the words are:")
for i in range(0,n):
   b=a[i]
   list.append(b)
print(list)
print("ordinal values in the given words are")
for i in range(0,n):
   c=ord(list[i])
print(c)
