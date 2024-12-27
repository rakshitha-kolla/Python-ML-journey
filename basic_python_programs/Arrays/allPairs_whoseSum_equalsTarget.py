def allpairs(arr1,target):
    seen=set()
    pairs=set()
    for num in arr1:
        compliment=target-num
        if compliment in seen:
            pairs.add((min(num,compliment),max(num,compliment)))
        seen.add(num)
    print(pairs)
import array as arr
arr1=arr.array("i")
n=int(input("Enter number of elements in array: "))
for i in range(n):
    ele=int(input("Enter element: "))
    arr1.append(ele)
target=int(input("Enter target: "))
allpairs(arr1,target)