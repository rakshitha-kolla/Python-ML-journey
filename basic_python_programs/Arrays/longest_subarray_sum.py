# find the length of the longest subarray with a given sum
def longest_subarray(arr,sum):
    prefix_sum={}
    cumulative_sum=0
    max_length=0
    for i in range(len(arr)):
        cumulative_sum+=arr[i]
        if cumulative_sum==sum:
           max_length=i+1
        if (cumulative_sum-sum) in prefix_sum:
            max_length=max(max_length,i-prefix_sum[cumulative_sum-sum])
        if cumulative_sum not in prefix_sum:
            prefix_sum[cumulative_sum]=i
    print(prefix_sum)
    print(max_length)
arr=list(map(int,input("Enter elements of array with spaces: ").split()))
print(arr)
sum=int(input("Enter sum: "))
longest_subarray(arr,sum)