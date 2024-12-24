## subset of given array or set
def calcsubset(arr,res,subset,index):
	res.append(subset[:])
	for i in range(index,len(arr)):
		subset.append(arr[i])
		calcsubset(arr,res,subset,i+1)
		subset.pop()
def subsets(arr):
	subset=[]
	res=[]
	index=0
	calcsubset(arr,res,subset,index)
	return res
A=[1,2,3]
res=subsets(A)
for i in res:
	print(i)
