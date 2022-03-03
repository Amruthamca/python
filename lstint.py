n1=[10,8,30,60]
n2=[20,4,56,10,76]
len1=len(n1)
len2=len(n2)
if(len1==len2):
    print("same of length")
else:
    print("not same of length")
sumn1=0
sumn2=0
for i in n1:
    sumn1=sumn1+i
for i in n2:
    sumn2=sumn2+i
if(sumn1==sumn2):
    print("both are of equal sum")
else:
    print("are not of equal length")
for x in n1:
    if(x in n1 and x in n2):
        print(x)
