d1={}
n1=int(input("enter limit in 1st dictionary"))
print("enter dictionary value")
for i in range(0,n1):
    key=input("key:")
    value=input("values:")
    d1.update({key:value})
d2={}
n2=int(input("enter limit in 1st dictionary"))
print("enter dictionary value")
for i in range(0,n2):
    key=input("key:")
    value=input("values:")
    d2.update({key:value})
print("first dictionary:",d1)
print("second dictionary:",d2)
d3={}
for i in (d1,d2):
    d3.update(i)
print("merged dictionary is",d3)
