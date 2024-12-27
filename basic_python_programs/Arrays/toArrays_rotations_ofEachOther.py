# check if two arrays are rotations of each other
def rotations(arr1,arr2):
    if len(arr1) != len(arr2):
        return False
    str1="".join(map(str,arr1))
    str2="".join(map(str,arr2))
    combined=str1+str1
    return (str2 in combined)
import array as arr
arr1=arr.array("i")
arr2=arr.array("i")
n1=int(input("Enter num of elements in array1: "))
n2=int(input("Enter num of elements in array2: "))
for i in range(n1):
    ele=int(input("Enter elements of array1: "))
    arr1.append(ele)
for i in range(n2):
    ele=int(input("Enter elements of array2: "))
    arr2.append(ele)
if rotations(arr1,arr2):
    print("they are rotations to each other")
else:
    print("they are not rotations to each other")