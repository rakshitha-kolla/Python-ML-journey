import array as arr
def second_large(a):
    if(len(a)<2):
        return "Array must have atleast two elements"
    t=-10000000000000000000
    largest=second_largest=t
    for num in a:
        if num>largest:
            second_largest=largest
            largest = num
        elif num>second_largest and num != largest:
            second_largest=num
    if second_largest==-10000000000000000000:
        return "no second largest"
    return second_largest
a=arr.array("i")
n=int(input("Enter number of elements: "))
for i in range(n):
    ele=int(input("Enter element: "))
    a.append(ele)
print(a)
print(second_large(a))