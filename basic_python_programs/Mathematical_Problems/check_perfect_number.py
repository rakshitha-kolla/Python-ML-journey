'''
perfect number is a positive number that is equal to the sum of all its proper divisors or factors
i.e sum of all its factors excluding itself
6 = 1,2,3
28= 1,2,4,7,14
'''
def check_perfect(n):
    factors=[]
    for i in range(1,n):
        if n%i == 0:
            factors.append(i)
    sum=0
    for i in factors:
        sum+=i
    print(factors)
    if sum==n:
        print(f"{n} is perfect number")
    else:
        print(f"{n} is not perfect")

n=int(input("Enter number: "))
check_perfect(n)
