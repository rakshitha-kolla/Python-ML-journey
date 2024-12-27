## toggle the kth bit of a number
def toggle(n,k):
    return n^(1<<(k-1))
n=int(input("Enter number: "))
k=int(input("Enter bit u want to toggle: "))
t=toggle(n,k)
print(f"num {n} after toggling {k}th bit is {t}")