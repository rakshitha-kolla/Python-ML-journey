## find only non-repeated number in an array where every other number repeats twice
def non_repeated(arr):
    result=0
    for ele in arr:
        result=result^ele
    print(f"non repeating number is {result} ")
n=int(input("Enter number of elements: "))
arr=[]
for i in range(n):
    e=int(input("Enter element: "))
    arr.append(e)
non_repeated(arr)