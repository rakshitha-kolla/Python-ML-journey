#method 1
'''a,b=2,3
print("a=",a,"b=",b)
temp=a
a=b
b=temp
print('a=',a,'b=',b)'''
#print("a=" + a) give "type error"
#method2 without using third variable
'''a,b=3,4
print("a=",a,"b=",b)
a,b=b,a
print("a=",a,"b=",b)'''

#method3 using addition
'''
a,b=4,3
print("a=",a,"b=",b)
a=a+b
b=a-b
a=a-b
print("a=",a,"b=",b)
'''
a,b=3,4
print(a,b)