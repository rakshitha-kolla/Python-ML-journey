'''
armstrong number is a number that is equal to sum of its digits rised to the power of number of digits
example: 0,1,2,3,4,5,6,7,8,9,153,370,371,407
'''
def check_armstrong(n):
    string=str(n)
    l=len(string)
    sum=0
    for s in string:
        sum+=(int(s)**l)
    if sum==n:
        print(f"{n} is armstrong number")
    else:
        print(f"{n} is not armstrong number")
n=int(input("Enter number: "))
check_armstrong(n)