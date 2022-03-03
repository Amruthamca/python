n1=int(input("Enter the first number"))
n2=int(input("Enter the last number"))
for i in range(n1,n2):
    for j in range(32,100,1):
        if i==j*j:
            string=str(i)
            if int(string[0])%2==0 and int(string[1])%2==0 and int(string[2])%2==0 and int(string[3])%2==0:
                print(i)
