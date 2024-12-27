def count(n):
    c=0
    while(n):
        n = n & (n-1)
        c+=1
    return c
n=int(input("Enter number: "))
c=count(n)
print(f"number of bits in {n} are {c}")
