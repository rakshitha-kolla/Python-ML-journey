def firstN_perfect(n):
    if n<0:
        print("not possible")
        return
    elif(n==1 or n==1):
        print(f"{n} is not a perfect number")
        return
    c=0
    i=2
    perfect=[]
    while(c<n):
        factors=[]
        sum=0
        for j in range(1,i):
            if i%j==0:
                sum+=j
        if sum==i:
            perfect.append(i)
            c+=1
        i+=1
    print(perfect)
n=int(input("Enter n: "))
firstN_perfect(n)