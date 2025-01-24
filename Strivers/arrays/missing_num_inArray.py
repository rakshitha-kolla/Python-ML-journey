def missing(arr,n):
    for i in range(1,n+1):
        if i not in arr:
            return f"{i} is missing"
    return "no number misisng"
if __name__=="__main__":
    arr=list(map(int,input("Enter elements: ").split()))
    print(arr)
    n=int(input("range: "))
    print(missing(arr,n))