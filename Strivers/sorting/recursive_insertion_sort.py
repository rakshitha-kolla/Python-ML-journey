def insertion_sort(arr,i,n):
    if i>n-1:
        return
    j=i-1
    key=arr[i]
    while(j>=0 and arr[j]>key):
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=key
    insertion_sort(arr,i+1,n)
if __name__=="__main__":
    arr=list(map(int,input("Enter elements: ").split()))
    print("before sorting: ",arr)
    n=len(arr)
    insertion_sort(arr,1,n)
    print("after sortin: ",arr)