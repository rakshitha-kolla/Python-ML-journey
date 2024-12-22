n= int(input("Enter num of rows: "))
m=int(input("ENter no of coumns: "))
for i in range(n,0,-1):
	print(2*(n-i)*" ",end="")
	for j in range(m):
		print("*",end=" ")
	print()

