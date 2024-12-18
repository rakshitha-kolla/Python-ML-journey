'''
 * * * * * * * * *
    * * * * * * *
      * * * * *
        * * *
          *
        * * *
      * * * * *
    * * * * * * *
  * * * * * * * * *

'''
n=int(input("Enter num of rows: "))
for i in range(n-1,0,-1):
    print((n-i)*"  ",end="")
    for j in range(2*i+1):
        print("*",end=" ")
    print()
for i in range(n):
    print((n-i)*"  ",end="")
    for j in range(2*i+1):
        print("*",end=" ")
    print()

#num hour glass
for i in range(n-1,0,-1):
    print((n-i)*"  ",end="")
    for j in range(1,2*i+2):
        print(j,end=" ")
    print()
for i in range(n):
    print((n-i)*"  ",end="")
    for j in range(1,2*i+2):
        print(j,end=" ")
    print()

#alphabets
for i in range(n-1,0,-1):
    print((n-i)*"  ",end="")
    for j in range(0,2*i+1):
        print(chr(65+j),end=" ")
    print()
for i in range(n):
    print((n-i)*"  ",end="")
    for j in range(0,2*i+1):
        print(chr(65+j),end=" ")
    print()