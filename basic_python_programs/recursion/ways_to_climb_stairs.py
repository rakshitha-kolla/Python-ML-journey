## count number of ways to climb n stairs with steps of 1 or 2
def count_ways(n):
    if n==0 or n==1:
        return 1
    return count_ways(n-1)+count_ways(n-2)
n=int(input("Enter n: "))
print(count_ways(n))