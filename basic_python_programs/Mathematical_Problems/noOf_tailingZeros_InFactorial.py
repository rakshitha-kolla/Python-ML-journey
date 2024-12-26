def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)
def tailingZeros(n):
    fact=factorial(n)
    t=0
    temp=fact
    print(fact)
    while(temp):
        r=temp%10
        temp=temp//10
        if r==0:
            t+=1
    return t
n=int(input("Enter number: "))
z=tailingZeros(n)
print(f"no of tailing zeros in factorial of {n} are {z}")