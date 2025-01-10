
def maximum(arr):
    max_len=0
    c=0
    for num in arr:
        if num==1:
            c+=1
            max_len=max(c,max_len)
        else:
            c=0
    return max_len
if __name__=="__main__":
    arr=list(map(int,input("Enter elements: ").split()))
    print(arr)
    m=maximum(arr)
    print(m)