n=int(input("no of students: "))
stu=[]
for i in range(n):
    e=input("enter emain id: ")
    stu.append(e)
t=tuple(stu)
l1=[]
l2=[]
print(t)
for i in t:
    l=i.split('@')
    l1.append(l[0])
    l2.append(l[1])
t1=tuple(l1)
t2=tuple(l2)
print(t1)
print(t2)




n=int(input("enter the no.of students email id you want to enter:"))
list=[]
username=[]
domain=[]
for i in range(n):
    a=input("enter the email_id:")
    list.append(a)
tuple1=tuple(list)
for i in list:
    l=i.index("@")
    b=i[0:l:1]
    c=i[l+1:len(i):1]
    username.append(b)
    domain.append(c)
tuple2=tuple(username)
tuple3=tuple(domain)
print("\nThe tuple with the mail_ids is :")
for i in range(n):
    print(tuple1[i],end=" ")
print("\nThe tuple with the usernames is :")
for i in range(n):
    print(tuple2[i],end=" ")
print("\nThe tuple with the domains is :")
for i in range(n):
    print(tuple3[i],end=" ")
