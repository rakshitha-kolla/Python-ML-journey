#Longest Subarray with given Sum K(Positives)

def longest_subarray(arr,s):
    n=len(arr)
    sum=0
    map={}
    max_len=0
    for i in range(n):
        sum+=arr[i]
        if sum==s:
            max_len=max(max_len,i+1)
        if sum-s in map:
            max_len=max(max_len,i-map[sum-s])
        if sum not in map:
            map[sum]=i
    return max_len

if __name__=="__main__":
    arr=list(map(int,input("Enter elements: ").split()))
    print(arr)
    s=int(input("enter sum: "))
    print(longest_subarray(arr,s))