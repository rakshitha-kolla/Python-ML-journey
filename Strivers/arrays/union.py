
def union(arr1,arr2):
    union_list=arr1[:]
    for ele in arr2:
        if ele not in union_list:
            union_list.append(ele)
    print(union_list)
if __name__=="__main__":
    arr1=list(map(int,input("Enter elements of arr1: ").split()))
    arr2 = list(map(int, input("Enter elements of arr2: ").split()))
    print(arr1)
    print(arr2)
    union(arr1,arr2)