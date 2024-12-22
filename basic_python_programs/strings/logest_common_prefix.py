'''strs=["flower","flow","fligh"]
l=len(strs)
out=''
sorted_strings=sorted(strs)
print(sorted_strings)
s1=sorted_strings[0]
s2=sorted_strings[-1]
l1=len(s1)
l2=len(s2)
min_length=min(l1,l2)
for i in range(min_length):
	if s1[i]==s2[i]:
		out+=s1[i]
	else:
		break
print(out)'''
## method 1 is order O(nlogn) due to sorting
## method2 O(m*n)
def longest_common_prefix(strs):
	shortest=min(strs,key=len)
	pre=""
	for i in range(len(shortest)):
		c=shortest[i]
		for s in strs:
			if s[i]!=c:
				pre=shortest[:i]
				return pre

strs=["geeksforgeeks","geeks","geek","geezer"]
pre=longest_common_prefix(strs)
print(pre)
strs=["flower","flow","fligh"]
print(longest_common_prefix(strs))
