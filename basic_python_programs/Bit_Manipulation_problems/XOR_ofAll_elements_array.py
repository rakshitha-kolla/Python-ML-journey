def XOR(arr):
    result=0
    for ele in arr:
        result=result^ele
    return result
n=int(input("Enter number of elements of array: "))
arr=[]
for i in range(n):
    e=int(input("Enter element: "))
    arr.append(e)
print(XOR(arr))
