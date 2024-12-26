def print_prime(n):
    sum=0
    if n<0:
        return
    if n==0 or n==1:
        return
    for i in range(2,n+1):
        j=i
        for j in range(2,i+1):
            if i%j==0:
                break
        if j==i:
            sum+=i
    return sum

n=int(input("Enter n: "))
s=print_prime(n)
print(f"sum of prime numbers upto {n} is : {s}")