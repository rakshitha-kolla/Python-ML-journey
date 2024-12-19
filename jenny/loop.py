'''
list=[1,2,3,4,5]
for i in list:
    print(i)
    if i==3:
        break
else:
    print("successfully executed")
print("bye")
'''

'''
# caculate average height from list of height 
# not use len(),sum()
#take input form user
# output should be rounded to whole num
height=input("Eneter heights seperated by comma ',' : ")
list=height.split(',')
count=0
for i in list:
    count+=1
sum=0
for i in range(count):
    list[i]=int(list[i])
    sum+=list[i]
print(list)
print(sum)
avg=sum/count
print(avg)
print("avg= ",round(avg))
'''

# find max num from list of numbers
# input from user 
# not use max() fun
# use split,range fun
'''
num=input("eneter numbers seperated by space: ")
list=num.split()
print(list)
count=0
for i in list:
    count+=1
max=0
for i in range(count):
    list[i]=int(list[i])
    if(max<=list[i]):
        max=list[i]
print(max)    
'''

'''
#wtp print num from 1 to 100
# if num div by 3 print fizz
#if num dicv by 5 print buzz
# if div by both print fizz buzz
# else print num as it is
for i in range(1,101):
    if((i%5==0)and(i%3==0)):
        print("fizz buzz")
    elif(i%3==0):
        print("fizz")
    elif(i%5==0):
        print("buzz")
    else:
        print(i)
'''
print("hello \rwor")










