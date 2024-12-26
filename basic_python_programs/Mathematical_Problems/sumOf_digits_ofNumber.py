'''
n=1234
step1= 1+2+3+4 = 10
step2= 1+0 =1
output=1
'''

def sum_of_digits(n):
    if  n<9:
        print(sum=0)
        return
    sum=0
    temp=n
    while(temp>0 or sum>9):
        r=temp%10
        temp=temp//10
        sum+=r
        if temp==0 and sum>9:
            temp=sum
            sum=0
    print(f"sum of digits of {n} until it becomes single digit is {sum}")
n=int(input("enter number: "))
sum_of_digits(n)