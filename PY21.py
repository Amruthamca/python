list1=[]
list2=[]
n1=int(input("Enter the number of elements"))
print("Enter integers")
for i in range(0,n1):
    a=int(input())
    list1.append(a)
print(list1)
print("Square of numbers")
for square in list1:
    square=square*square
    list2.append(square)
print(list2)

