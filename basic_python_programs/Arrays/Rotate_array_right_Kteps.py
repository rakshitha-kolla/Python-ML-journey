import array as arr
def rotate(a,k):
    k=k%len(a)
    rotated_arr=a[-k:]+a[:-k]
    print(rotated_arr)
a=arr.array("i")
n=int(input("Enter number of elements: "))
for i in range(n):
    ele=int(input("Enter element: "))
    a.append(ele)
print(a)
k=int(input("enter steps you want to move right: "))
rotate(a,k)