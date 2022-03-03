list1=[]
list2=[]
n1=int(input("Enter the number of elements"))
print("Enter integers")
for i in range(0,n1):
    a=int(input())
    list1.append(a)
print(list1)
print("List of positive numbers")
for i in list1:
    if(i>=0):
        list2.append(i)
print(list2)

