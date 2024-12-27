'''def check_power(n):
    temp=n
    if n<=0:
        return False
    while(temp%2==0):
        temp=temp//2
    return temp==1
n=int(input("Enter number: "))
if check_power(n):
    print(f"{n} is power of 2")
else:
    print(f"{n} is not power of 2")
'''
#using bit manupulation
## n&(n-1)==0 then number is power of 2
## if we subtract power of 2 number by 1 then all unset bits after the only set bit becomes set and set bits becomes unset
## 4=100 3=011
## 16=10000 15 =01111
## we use bitwise and of n and n-1 will be zero if n is power of 2
def check_power(n):
    if n>0 and (n)&(n-1)==0:
        return True
    return False
n=int(input("Enter number: "))
if check_power(n):
    print(f"{n} is power of 2")
else:
    print(f"{n} is not a power of 2")