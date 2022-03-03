snt=input("enter the sentence")
spltsent=snt.split()
setsnt=set(spltsent)
dict={}
for i in setsnt:
x=snt.count(i)
dict.update({i:x})
print(dict)
