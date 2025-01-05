def bubble_sort(arr,n):
    if n<1:
        return
    for j in range(n-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
    bubble_sort(arr,n-1)
if __name__=="__main__":
    arr=list(map(int,input("Enter elements: ").split()))
    print("before sorting: ",arr)
    n=len(arr)
    bubble_sort(arr,n)
    print("after sortin: ",arr)