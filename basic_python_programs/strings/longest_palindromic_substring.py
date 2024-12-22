def longest_pal(s):
	res=""
	reslen=0
	for i in range(len(s)):
		##odd
		l=i
		r=i
		while(l>=0 and r<len(s) and s[l]==s[r]):
			if (r-l+1)>reslen:
				res=s[l:r+1]
				reslen=r-l+1
			r+=1
			l-=1
		##Even
		l=i
		r=i+1
		while(l>=0 and r<len(s) and s[l]==s[r]):
			if (r-l+1)>reslen:
				res=s[l:r+1]
				reslen=r-l+1
			r+=1
			l-=1
	print(res)
		


string=input("Enter string: ")
longest_pal(string)
