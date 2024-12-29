n=int(input("Enter n: "))
char="A"
for i in range(n):
    for j in range(i+1):
        if(i % 2 == 0 and j % 2==0) or (i % 2 != 0 and j % 2 != 0):
            print(char.upper(),end=" ")
        else:
            print(char.lower(),end=" ")
        char=chr(ord(char)+1)
    print()
