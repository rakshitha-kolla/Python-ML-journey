### greatest common devisor 
## 45=3*3*5
## 30=2*3*5
## common=3*5
## gcd=15


## using recursion
def rec_gcd(a,b):
	if b>a:
		b=b-a
	elif a>b:
		a=a-b
	if a==b:
		return a
	return rec_gcd(a,b)
## normal method
def gcd(a,b):
    term=1
    m=min(a,b)
    for i in range(m,0,-1):
        if a%i == 0 and b%i == 0:
            return i


a=int(input("Enter a: "))
b=int(input("Enter b: "))
print(rec_gcd(a,b))
gcd(a,b)

