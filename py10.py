import operator
d1 = {}
n = int(input("size of dictionary"))
print("Enter data :")
for i in range(0,n,1):
   key = input("key : ")
   value = input("value : ")
   d1.update({key : value})

print("dictionary is ",d1)
asc = sorted(d1.items(),key=operator.itemgetter(1))
dsc = sorted(d1.items(),key=operator.itemgetter(1),reverse=True)
print("ascending",asc)
print("descending",dsc)