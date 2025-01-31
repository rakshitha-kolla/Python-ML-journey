'''Problem Statement: Given an integer array arr,
find the contiguous subarray (containing at least one number) which
has the largest sum and returns its sum and prints the subarray.'''
a=list(map(int,input("Enter array elements seperated by , ").split(",")))
print(a)
dict={}
l=0
sum=0
idx=[]
for i in range(len(a)):
    sum+=a[i]
    dict[i]=sum
for k in dict:
    if dict[k]>l:
        l=dict[k]
        idx=[0,k]
    if k>0:
        t=0
        while(t < k):
            if (dict[k]-dict[t]) > l:
                l=dict[k]-dict[t]
                idx=[t+1,k]
            t+=1
print(l)
print(a[idx[0]:idx[1]+1])