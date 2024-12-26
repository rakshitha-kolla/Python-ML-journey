def check_prime(n):
    if n<0:
        return "invalid"
    if n == 1 or n==0:
        return f"{n} is neither prime nor composite"
    i=1
    for i in range(2,n):
        if n%i==0:
            break
    if i==n-1:
        return f"{n} is prime"
    else:
        return f"{n} is not prime"
n=int(input("Enter number: "))
print(check_prime(n))