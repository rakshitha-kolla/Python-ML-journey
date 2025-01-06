'''Two Sum : Check if a pair with given sum exists in Array

Problem Statement: Given an array of integers arr[] and an integer target. '''
def two_sum(arr,t):
    seen={}
    for i in range(len(arr)):
        complement=t-arr[i]
        if complement in seen:
            return (seen[complement],i)

        seen[arr[i]]=i
    return None

if __name__=="__main__":
    arr=list(map(int,input("ENter elements: ").split()))
    print(arr)
    t=int(input("Enetr target: "))
    result=two_sum(arr,t)
    if result:
        print(f"Exists at index {result[0]} and {result[1]}")
    else:
        print("doesnot exist")