arr=list(map(int,input("Enetr elements seperated by space: ").split()))
print(arr)
n=len(arr)
for i in range(1,n):
    j=i-1
    key=arr[i]
    while(j>=0 and arr[j]>key):
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=key
print(arr)