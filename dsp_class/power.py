def power(b,e):
    p=1
    for i in range(e):
        p=p*b
    return p
base=int(input("enter base: "))
exp=int(input("enter exp: "))
p=power(base,exp)
print(p)