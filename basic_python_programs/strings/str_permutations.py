## all permutations of string
def swap(s,idx,i):
	s=list(s)
	temp=s[idx]
	s[idx]=s[i]
	s[i]=temp
	return "".join(s)
def permuterec(s,idx):
	if idx==len(s)-1:
		print(s)
		return
	for i in range(idx,len(s)):
		s=swap(s,idx,i)
		permuterec(s,idx+1)
		s=swap(s,idx,i)
def permute(s):
	permuterec(s,0)
string=input("Enter string: ")
permute(string)
