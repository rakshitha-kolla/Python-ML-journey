
def linear_search(arr,ele):
    for i in range(len(arr)):
        if arr[i]==ele:
            return i
    return -1
if __name__=="__main__":
    arr=list(map(int,input("Enter elements: ").split()))
    print(arr)
    ele=int(input("Enter element to search: "))
    idx=linear_search(arr,ele)
    if idx==-1:
        print("not found")
    else:
        print(f"{ele} found at index {idx}")