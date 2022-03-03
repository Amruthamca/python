d1={}
n1=int(input("enter limit in 1st dictionary"))
print("enter dictionary value")
for i in range(0,n1):
    key=input("key:")
    value=input("values:")
    d1.update({key:value})
print("dictionary is=",d1)
asc=sorted(d1.items(),key=operator.itemgetter(1))
dsc=sorted(d1.items(),key=operator.itemgetter(1),reverse=True)
print("ascending order=",asc)
print("descending order=",dsc)