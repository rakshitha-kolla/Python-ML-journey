'''
Problem Statement:

There’s an array ‘A’ of size ‘N’ with an equal number of positive and negative elements.
Without altering the relative order of positive and negative elements,
 you must return an array of alternately positive and negative values.
 Input:
arr[] = {1,2,-4,-5}, N = 4
Output:
1 -4 2 -5
'''
pos=[]
neg=[]
a=list(map(int,input("Enter numbers seperated by comma : ").split(",")))
print(a)
for i in a:
    if i > 0:
        pos.append(i)
    else:
        neg.append(i)
c=0
while c < len(a):
    if c % 2==0:
        a[c]=pos.pop(0)
    else:
        a[c]=neg.pop(0)
    c+=1
print(a)