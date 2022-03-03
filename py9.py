list1=[]
list2=[]
n=int(input("enter limit"))
print("enter numbers")
for i in range(0,n):
    a=int(input())
    list1.append(a)
print(list1)
print("list after removing even numbers")
for i in range(0,n):
    if(list1[i]%2!=0):
        list2.append(list1[i])

print(list2)