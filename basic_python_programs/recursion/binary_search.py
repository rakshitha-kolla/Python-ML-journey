def sort(a):
    l=len(a)
    for i in range(1,l):
        key=a[i]
        j=i-1
        while j>=0 and key < a[j]:
            a[j+1]=a[j]
            j-=1
        a[j+1]=key
def binary_search(ele,arr,start,end):
    if start>end:
        return "not found"
    else:
        mid=(end+start)//2
        if ele==arr[mid]:
            return f"found at position {mid} "
        elif ele<arr[mid]:
            end=mid-1
        else:
            start=mid+1
    return binary_search(ele,arr,start,end)
n=int(input("number of elemenets: "))
arr=[]
for i in range(n):
    e=int(input(f"Enetr element{i} :"))
    arr.append(e)
print(arr)
ele=int(input("Enetr element u want to search: "))
sort(arr)
print(arr)
print(binary_search(ele,arr,0,len(arr)-1))