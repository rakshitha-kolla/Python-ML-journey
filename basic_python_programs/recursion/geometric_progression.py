## find nth term of geometric progression using recursion
## non recursion method
def geometric(a,r,n):
	if a<=0:
		return "invalid"
	term=a
	print("gp is ",a,end=" ")
	for i in range(1,n):
		term=term*r
		print(term,end=" ")
	return term

## using recursion
def recursive_gp(term,r,n,idx):
	print(term,end=" ")
	if idx>n-1:
		print("\nnth term of gp is: ",term)
		return
	term = term * r
	recursive_gp(term,r,n,idx+1)
def rec(a,r,n):
	term=a
	print("gp is: ",end=" ")
	recursive_gp(term,r,n,1)
a=int(input("Enter a: "))
r=float(input("Enter r: "))
n=int(input("Enter n: "))
nth=geometric(a,r,n)
print("\n",nth)
rec(a,r,n)
