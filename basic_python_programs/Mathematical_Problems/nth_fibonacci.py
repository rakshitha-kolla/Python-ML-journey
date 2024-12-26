def fibonacci(n):
    if n==0 or n==1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)
n=int(input('Enter number: '))
for i in range(n):
    print(fibonacci(i),end=" ")
print()
print(f"{n}th fibonacci number is {fibonacci(n-1)}")