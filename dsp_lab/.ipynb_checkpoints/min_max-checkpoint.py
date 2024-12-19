#list z=[1,2,3] or z=["rakshi","cat","rat"] or z=[3,"rakshi",2.0]
list = [] 
for i in range(0,5):
    ele=int(input("ENTER ELEMENT: " ))
    list.append(ele)
print(list)
#to find min value
min=1000000000000
max=0
for i in range(0,5):
    if(list[i] <= min):
        min=list[i]
    if(list[i] >= max):
        max=list[i]
print("min= ",min," max= ",max)