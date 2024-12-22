## freqency of each character in string
str=input("Enter string: ")
dict={}
for c in str:
	if c!=" ":
		if c in dict:
			dict[c]+=1
		else:
			dict[c]=1
print(dict)
