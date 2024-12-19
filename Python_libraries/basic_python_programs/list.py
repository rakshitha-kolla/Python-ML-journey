'''35. Create List with Range Concatenation

Write a Python program to create a list by concatenating a given list with a range from 1 to n.
Sample list : ['p', 'q']
n =5
Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']'''
'''
n=5
s=["p","q"]
so=[f"{s[0]}{i},{s[1]}{i}" for i in range(n)]
print(so)
sout=[]
for i in range(n):
    sout.extend([s[0]+f"{i}",s[1]+f"{i}"])
print(sout)
'''
'''2. Generate Groups of Consecutive Numbers

Write a Python program to generate groups of five consecutive numbers in a list. '''
i=0
l=[[5*i+j for j in range(1,6)] for i in range(5)]
print(l)