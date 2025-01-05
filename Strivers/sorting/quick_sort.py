def partition(arr,low,high):
    pivot=arr[low]
    i=low+1
    j=high
    while(i<j):
        while(i<high and arr[i]<=pivot):
            i+=1
        while(j>low and arr[j]>pivot):
            j-=1
        if i>j:
            break
        arr[i],arr[j]=arr[j],arr[i]
    arr[low],arr[j]=arr[j],arr[low]
    return j
def quick_sort(arr,low,high):
    if(low<high):
        p=partition(arr,low,high)
        quick_sort(arr,low,p-1)
        quick_sort(arr,p+1,high)
if __name__=="__main__":
    arr=list(map(int,input("Enter elemnts seperated by space: ").split()))
    print(arr)
    quick_sort(arr,0,len(arr)-1)
    print(arr)