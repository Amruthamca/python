n1=int(input("Enter the limit : "))
list=[]
print("Enter the names")
for i in range(0,n1):
    f=input()
    list.append(f)
print("Entered first names")
print(list)
sum=0
for i in list:
    sum=sum+i.count("a")
print(sum)

