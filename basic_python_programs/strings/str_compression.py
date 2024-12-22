## when a character is repeated k number of times concecutively like bbbb so encode as b4 for singlr character we shall not add the count into it
# ex: "abbbaaaaaaccdaaab" output: ab3a6c2da3b
string=input("Enter string: ")
out=""
c=1
for i in range(len(string)):
	if i < len(string)-1 and string[i]==string[i+1]:
		c+=1
	else:
		out+=string[i]
		if c>1:
			out+=str(c)
		c=1
print(out)
