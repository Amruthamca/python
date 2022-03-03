lmt=int(input("enter the limit"))
list1=[]
print("enter the numbers")
for i in range(lmt):
    n=int(input())
    if(n>100):
        list1.append("over")
    else:
        list1.append(n)
print(list1)
