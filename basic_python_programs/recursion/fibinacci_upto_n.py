def fibinacci(n):
	if n<0:
		return "invalid"
	elif n==0 or n==1:
		return n
	else:
		return fibinacci(n-1)+fibinacci(n-2)


n=int(input("Enter number upto which u want febinacci series: "))
for i in range(n):
	print(fibinacci(i),end=" ")

