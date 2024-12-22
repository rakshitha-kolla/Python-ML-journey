## anaragam is a phrase made by arranging the letters of another word or phrase
str1=input("Enter string: ")
str2=input("Enter string: ")
flag=0
str1=str1.replace(" ","").replace(".","").replace(",","").replace("'","")
str2=str2.replace(" ","").replace(".","").replace(",","").replace("'","")
dict1={}
dict2={}
if len(str1)!=len(str2):
	print("not anargams")
else:
	for c in str1:
		if c in dict1:
			dict1[c]+=1
		else:
			dict1[c]=1
	for c in str2:
		if c in dict2:
			dict2[c]+=1
		else:
			dict2[c]=1
	if dict1==dict2:
		print("anargams")
	else:
		print("not anargams")

