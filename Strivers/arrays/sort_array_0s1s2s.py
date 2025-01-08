'''Problem Statement: Given an array consisting of only 0s, 1s, and 2s. Write a program to in-place sort the array without using inbuilt sort functions. ( Expected: Single pass-O(N) and constant space)
'''
def sort_array(arr):
    low=0
    mid=0
    high=len(arr)-1
    while mid <= high:
        if arr[mid]==0:
            arr[low],arr[mid]=arr[mid],arr[low]
            low+=1
            mid+=1
        elif arr[mid]==1:
            mid+=1
        else:
            arr[mid],arr[high]=arr[high],arr[mid]
            high-=1
    print(arr)
if __name__=="__main__":
    arr=list(map(int,input("Enter array of only 0 1 2: ").split()))
    print(arr)
    sort_array(arr)
