l=["rakshi",25,[90,85,70,95,60],80]
print(l[3])
print(l[2][4])
print(l[1])
l[0]="cherry"
max=0
for i in l[2]:
    if(i>=max):
        max=i
print(max)