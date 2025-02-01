a=list(map(int,input().split(",")))
print(a)
min=10000000000
max=-1000000000
b=0
s=0
for i in range(len(a)):
    if i != len(a)-1:
        if a[i]<a[b]:
            b=i
            s=i
    if a[i]>a[s]:
        s=i
if b>s:
    print("0")
else:
    print(a[s]-a[b])
