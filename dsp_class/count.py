string=input("Enter string: ")
char=0
for i in string:
    char+=1
print("total no of char= ",char)
alpha=0
for i in string:
    if('A' <= i)and(i <= 'Z'):
        alpha+=1
    elif('a' <= i)and(i <= 'z'):
        alpha+=1
print("total no of alphabets=",alpha)
digit=0
for i in string:
    if(48<=ord(i))and(ord(i) <= 57):
        digit+=1
print("total no of degits=",digit)
spc=0
for i in string:
    if i.isalpha():
        continue
    elif i.isdigit():
        continue
    elif i.isspace():
        continue
    else:
        spc+=1
print("total no of special char=",spc)    
list=string.split()
words=len(list)
print("total no of words=",words)