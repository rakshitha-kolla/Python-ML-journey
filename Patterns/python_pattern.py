str="PYTHON"
l=len(str)
for i in range(l):
    for j in range(i+1):
        print(str[j],end=" ")
    print()
