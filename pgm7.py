#Amrutha Biju
#21mca003
with open("file.txt")as f:
	content_list=f.readlines()
content_list=[x.strip() for x in content_list]
print(content_list)



