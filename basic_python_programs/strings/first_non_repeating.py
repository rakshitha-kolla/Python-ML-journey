## find the first non-repeating character in a string
str=input("Enter string: ")
flag=0
for c in str:
	if str.count(c)==1:
		print(f"first non repeting char is {c}")
		flag=1
		break
	else:
		continue
if flag==0:
	print("$")
	
## using built in function is less efficient code it is O(n^2)
## method2
## dict are implemented using hash maps so oredr of checikng char in dict is O(1) so overall complexity is O(1)
dict={}
for c in str:
	if c in dict:
		dict[c]+=1
	else:
		dict[c]=1
flag=0
for c in dict:
	if dict[c]==1:
		print(f"first non repeating char is {c}")
		flag=1
		break
if flag==0:
	print("$")
