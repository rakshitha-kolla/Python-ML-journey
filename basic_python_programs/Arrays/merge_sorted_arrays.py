#merge sorted arrays into single sorted array
import array as arr
def merge(s1,s2,n,n2):
    merged=arr.array("i")
    l=min(n,n2)
    i=0
    k=0
    c=0
    while(k < n and c < n2 ):
        if s1[k]<s2[c]:
            merged.append(s1[k])
            k+=1
        else:
            merged.append(s2[c])
            c+=1
    if k < n:
        for i in range(k,n):
            merged.append(s1[i])
    else:
        for i in range(c,n2):
            merged.append(s2[i])
    print(merged)
def sort(a):
    for i in range(1,len(a)):
        j=i-1
        key=a[i]
        while(j>=0 and a[j]>key):
            a[j+1]=a[j]
            j-=1
        a[j+1]=key
    return a
arr1=arr.array("i")
n=int(input("Enter number of elements in array1: "))
for i in range(n):
    ele=int(input("Enter element: "))
    arr1.append(ele)
arr2=arr.array("i")
n2=int(input("Enter number of elements in array2: "))
for i in range(n2):
    ele=int(input("Enter element: "))
    arr2.append(ele)
print(arr1)
print(arr2)
sarr1=sort(arr1)
sarr2=sort(arr2)
print(sarr1)
print(sarr2)
merge(sarr1,sarr2,n,n2)
