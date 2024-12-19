import numpy as np
#A 1d array having aeiou
a=np.array(['a','e','i','o','u'])
print(a,"\n")

#C 2-D array having ones having 2 rows and 5 cols and alla elements are set to 1 amd dtype is str
a1=np.ones((2,5),dtype="str")
print(a1,"\n")

#D use nested python list to create 2-D array called myarray1 having 3 rows and 3 cols and store 
#2.7,-2,-19
#0,3.4,99.9
#10.6,0,13
myarray1=np.array([[2.7,-2,-19],[0,3.4,99.9],[10.6,0,13]])
print(myarray1,"\n")

#e
r=3
c=5
myarray2=np.arange(4,4+(r*c*4),4,dtype=float)
print(myarray2)
myarray2=myarray2.reshape((r,c))
print(myarray2,"\n")

# f  array_slpit unequal slipt
#np.split(array,no of rows) for equal slpit
#np.split(array,cols,axis=1)
#result=np.array_split(myarray4,3,axis=1) cols wise split
myarray4=np.arange(-1,-1+42*0.25,0.25).reshape((14,3))
print(myarray4)
result=np.array_split(myarray4,3)
print(result,"\n")
print(myarray4.sum(),"\t",myarray4.sum(axis=0),"\t",myarray4.sum(axis=1),"\n")
print(myarray4.max(),"\t",myarray4.max(axis=0),"\t",myarray4.max(axis=1),"\n")
print(myarray4.min(),"\t",myarray4.min(axis=0),"\t",myarray4.min(axis=1),"\n")
print(myarray4.mean(),"\t",myarray4.mean(axis=0),"\t",myarray4.mean(axis=1),"\n")
print(myarray4.std(),"\t",myarray4.std(axis=0),"\t",myarray4.std(axis=1),"\n")
print(myarray4/3)
print(myarray4)
#print(myarray1+myarray2) not posiible
myarray3=myarray1@myarray2
print(myarray3)
