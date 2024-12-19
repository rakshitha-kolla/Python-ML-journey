def febi(n):
    if n<=1:
        return n
    else:
        return (febi(n-1)+febi(n-2))
n=int(input("enter which febi num u want"))
if n<=0:
    print("pls eneter valid n: ")
else:
    print("febinocci series:")
    for i in range(n):
        print(febi(i))
    
    