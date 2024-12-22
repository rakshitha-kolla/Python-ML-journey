str=input("Enter string: ")
n=len(str)
flag=1
print(n//2)
for i in range(n//2):
	if str[i]==str[n-(i+1)]:
		continue
	else:
		print(f"{str} is not palindrome")
		flag=0
		break
if flag==1:
	print(f"{str} is palindrome")

