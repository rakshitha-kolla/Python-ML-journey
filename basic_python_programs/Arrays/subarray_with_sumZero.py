# determine if an array contains a subarray with a sum of zero
def sumZero(arr):
    presum=set()
    cumulative_sum=0
    for i in range(len(arr)):
        cumulative_sum+=arr[i]
        if cumulative_sum==0 or cumulative_sum in presum:
            return True
        presum.add(cumulative_sum)
    return False
arr=list(map(int,input("Enter elements of array with spaces: ").split()))
print(arr)
if sumZero(arr):
    print("Exists")
else:
    print("does not exist")