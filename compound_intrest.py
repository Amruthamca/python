import math
p=float(input("enter principle amount"))
r=float(input("enter rate of intrest"))
n=float(input("enter number of years"))
A=p*(1+r/100)**n
c=math.pow(A,0)
compound_intrest=A-c
print("priciple amount=",p)
print("rate of intrest=",r)
print("number of years=",n)
print("compound intrest=",compound_intrest)

