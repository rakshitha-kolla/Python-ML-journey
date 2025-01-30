'''Problem Statement: Given an array of N integers,
write a program to return an element that occurs more than N/2 times in the given array.
You may consider that such an element always exists in the array.'''

nums=list(map(int,input().split(",")))
print(nums)
N=len(nums)
count={}
for i in nums:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print(count)
for i in count:
    if count[i] > N/2:
        print(i)
        break


## optimized approch
nums=list(map(int,input().split(",")))
print(nums)
N=len(nums)
element=nums[0]
c=0
for i in range(N):
    if c==0:
        element=nums[i]
        c+=1
    else:
        if nums[i] == element:
            c+=1
        else:
            c-=1
print(element)