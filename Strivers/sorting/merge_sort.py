
def merge(arr,low,mid,high):
    temp=[]
    left=low
    right=mid+1
    while(left<=mid and right<=high):
        if arr[left]>arr[right]:
            temp.append(arr[right])
            right+=1
        else:
            temp.append(arr[left])
            left+=1
    while(left<=mid):
        temp.append(arr[left])
        left+=1
    while(right<=high):
        temp.append(arr[right])
        right+=1
    i=0
    while(low<=high):
        arr[low]=temp[i]
        low+=1
        i+=1
def merge_sort(arr,low,high):
    if low>=high:
        return
    mid=(low+high)//2
    merge_sort(arr,low,mid)
    merge_sort(arr,mid+1,high)
    merge(arr,low,mid,high)
if __name__=="__main__":
    arr=list(map(int,input("Enter elemnts seperated by space: ").split()))
    print(arr)
    merge_sort(arr,0,len(arr)-1)
    print(arr)