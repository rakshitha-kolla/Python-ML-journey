'''x=input("eneter first num: ")
y=input("enter 2nd num: ")
print(x[0],y[0])
sum=int(x)+int(y)
print(sum)
print(type(x))
x=123
print(type(x))'''

#SET

'''set={1,2,3,4,5,5,6,6,6}
#print(set{1}) gives error set is unordered so we can retrive set eliments using index  but we can use loop
print(len(set))
for i in set:
 print(i,end=" ")
set2={"rakshi",32,4.5,(1,2,3)}
for i in set2:
 print(type(i),end=" ")
print(set2)'''
#set3={1,2,{1:2,2:3}} we cannot include mutable datatypes inn set

#set operations
'''
set1={1,2,3}
set2={3,4,5}
print(set1|set2)#union
print(set1&set2)#intersection
print(set1-set2)#difference
set1.add(4)
print(set1)
#set1.clear()
set1.pop()
print(set1)
set3=set1.copy()
print(set3)
set3.discard(3)
print(set3)
set3.remove(2)
print(set3)
set3.update(set1)
print(set3)
set3={7,8,9}
print(set3)
'''

#lists
'''
list1=[1,2,"rakshi",(1,23)]
print(list1[3][1])
list2=[3,4,5]
list3=list1+list2
print(list3)
list1.append(3)
list1.extend([8,8])
print(list1)
list1.insert(1,"kolla")
print(list1)
list1.pop(1)
print(list1)
list1.remove(3)
print(list1)
list1.clear()
print(list1)
list1=list3.copy()
print(list1)
print(list1[-4:-6:-1])
print(list1.count(3))
print(list1.index(3))
list1.reverse()
print(list1)
list1.pop(3)
list1.pop(3)
list1.sort()
print(list1)
list1.sort(reverse=True)
print(list1)
'''

#dictinaries
'''
dict1={"name":"rakshi","age":23,"clg":"rgukt"}
print(dict1["name"])
dict2={1:2,2:3}
#dict3=dict1+dict2 gives error
dict2[5]="rakshi"
print(dict2)
dict2.update({15:"rakshi"})
print(dict2)
dict2[5]="kolla"
print(dict2)
dict2.pop(5)
print(dict2)
dict2.popitem()
print(dict2)
dict3=dict1.copy()
print(dict3)
dict3=dict(dict2)
print(dict3)
print(dict2.keys())
print(dict2.values())
print(dict2.items())
'''

#tuples

x=(1,1,2,3,4)
for i in x:
    print(i,end=" ")
print("\n",x.index(1))
print(x.count(1))
y=list(x)
y.pop(1)
print(y)
x=tuple(y)
print(x)
y=(0,9,8,7)
z=x+y
print(z)
z=x*2
print(z)
z=list(z)
print(z*2)
(green,*yellow,red)=x
print(green,yellow,red)
