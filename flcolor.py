list=[]
n=int(input("enter number of element in the list:"))
print("enter colors of the list")
for i in range(0,n):
    a=input()
    list.append(a)
print("list is:",list)
print("first color in the list is:",list[0])
print("last color in the list is:",list[-1])
