arr=list(map(int,input("Enter elements separted by space ").split()))
n=len(arr)
print("before sorting: ",arr)
for i in range(n-1):
    for j in range(n-1-i):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print("After sorintg: ",arr)