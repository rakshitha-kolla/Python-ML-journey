def move(arr):
    non_zero_index=0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[non_zero_index]=arr[i]
            non_zero_index+=1
    for j in range(non_zero_index,len(arr)):
        arr[j]=0
    print(arr)

if __name__=="__main__":
    arr=list(map(int,input("Enter elements: ").split()))
    print(arr)
    move(arr)