n=int(input("Enter n: "))
arr=[]
for i in range(n):
    ch=int(input("Enter element: "))
    arr.append(ch)
print("array before sorting: ",arr)
for i in range(n-1):
    min_idx=i
    for j in range(i+1,n):
        if arr[j]<arr[min_idx]:
            min_idx=j
    arr[i],arr[min_idx]=arr[min_idx],arr[i]
print("afetr sorting: ",arr)