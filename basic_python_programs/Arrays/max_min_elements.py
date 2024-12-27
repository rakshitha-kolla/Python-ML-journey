# find max and min elements of array
import array as arr
a=arr.array("i",[])
n=int(input("Enter number of elements: "))
for i in range(n):
    e=int(input("Enter element: "))
    a.append(e)
print(a)
print(min(a))
print(max(a))
min=1000000000000
max=-123456789890
for ele in a:
    if(min>ele):
        min=ele
    if(max<ele):
        max=ele
print(f"min={min},max={max}")
