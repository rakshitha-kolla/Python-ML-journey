def ispalindrome(n):
    l=list((map(int,str(n))))
    le=len(l)//2
    for i in range(le):
        if l[i] != l[-(i+1)]:
            print("not palindrome")
            return
    print("palindrome")
n=int(input("Enter number: "))
ispalindrome(n)