'''
15= 3*5
12= 2*2*3
315= 3*3*5*7
'''
import math
def prime_factors(n):
    temp=n
    factors=[]
    if temp % 2 == 0:
        factors.append(2)
        temp=temp//2
    for i in range(3,int(math.sqrt(temp))+1,2):
        while(temp % i == 0):
            factors.append(i)
            temp=temp//i
    if temp>2:
        factors.append(temp)
    print(factors)
n=int(input("Enter number: "))
prime_factors(n)