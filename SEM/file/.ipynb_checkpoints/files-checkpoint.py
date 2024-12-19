'''
f1=open("text.txt","w")
f1.write("hi this is rakshi\n")
f1.write("hello good morning rakshi")
f1.writelines(["rkvalley","nuzveedu",'ongole','srk'])
f1=open("text.txt","r+")
print(f1.tell())
f1.write("qwerty")
print(f1.tell())
print(f1.read())
print(f1.tell())
'''

f1=open("text3.txt","a+")
print(f1.tell())
f1.write("rakshi")
print(f1.tell())
f1=open("text.txt","a+")
print(f1.read())
print(f1.tell())
f1=open("text.txt","a+")
f1.seek(0)
print(f1.read())

'''
f1=open("text.txt","w")
b=["hello","how","are","you"]
f1.writelines(b)
f1=open("text.txt","r+")
f1.write("mnbvcx")
print(f1.read())'''
'''
f1=open("writeplus.txt","w+")
f1.write("kolla\n")
f1.write("rakshi")
print(f1.read())
f1.write("hello")
f1.seek(2,0)
print(f1.read())
f1.seek(0,0)
'''
print(f1.read())