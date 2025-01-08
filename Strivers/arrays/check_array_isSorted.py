def is_sorted(arr):
    n=len(arr)
    for j in range(1,n):
        if arr[j]<arr[j-1]:
            return False
    return True
if __name__=="__main__":
    arr=list(map(int,input("Enter elements: ").split()))
    if is_sorted(arr):
        print("array is sorted")
    else:
        print("array is not sorted")