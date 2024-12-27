import array as arr
def moveZero(arr1,n):
    index=0
    for i in range(len(arr1)):
        if arr1[i] != 0:
            arr1[index]=arr1[i]
            index+=1
    for i in range(index,n):
        arr1[i]=0
    print(arr1)
arr1=arr.array("i")
n=int(input("Enter number of elements in array1: "))
for i in range(n):
    ele=int(input("Enter element: "))
    arr1.append(ele)
moveZero(arr1,n)