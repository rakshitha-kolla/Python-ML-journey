import re
string="python is high level programming language,high expectations"
'''x=re.search("high",string)
print(x)
s=re.split("high",string)
f=re.findall("i",string)
print(f)
print(s)
m=re.match("python",string)
print(m)
m1=re.match("high",string)
print(m1)'''
string2="python"
f1=re.fullmatch("python",string)
f2=re.fullmatch("python",string2)
print(f1)
print(f2)
if f1:
    print("found")
else:
    print("not found")
if f2:
    print("match")
else:
    print("not match")
    