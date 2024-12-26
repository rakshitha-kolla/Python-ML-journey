def print_prime(n):
    if n<0:
        print("invalid")
        return
    print(f"prime numbers upto {n} are: ")
    if n==0 or n==1:
        print(f"{n} is neither prime nor composite")
    for i in range(2,n+1):
        j=i
        for j in range(2,i+1):
            if i%j==0:
                break
        if j==i:
            print(i,end=" ")
    return

n=int(input("Enter n: "))
print_prime(n)