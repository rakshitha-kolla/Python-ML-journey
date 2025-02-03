a=list(map(int,input().split(",")))
print(a)
max=-100000
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[j]-a[i]>max:
            max=a[j]-a[i]
print(max)

# optimal approch

maxp=0
min=10000000000
for i in range(len(a)):
    if a[i]<min:
        min=a[i]
    if a[i]-min>maxp:
        maxp=a[i]-min
print(maxp)