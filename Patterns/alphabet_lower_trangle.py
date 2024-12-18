'''
A
B C
D E F
G H I J
K L M N O
'''
n=int(input("Enter num of rows: "))
ch=65
print("pattern1: ")
for i in range(n):
    for j in range(i+1):
        print(chr(ch),end=" ")
        ch+=1
    print( )
print("pattern2: \n")
for i in range(n):
    for j in range(i+1):
        print(chr(65+i),end=" ")
    print()

print("pattern3: \n")
ch=65
for i in range(n):
    for j in range(2*i+1):
        print(chr(ch),end=" ")
        ch+=1
    print()