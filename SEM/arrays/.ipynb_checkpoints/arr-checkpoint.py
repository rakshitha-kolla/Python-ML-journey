import numpy as np
'''
#od
a1=np.array(2)
print(a1.ndim)
print(a1)
#1d 
a2=np.array([1,2,3.3])
print(a2)
print(a2.ndim,a2.shape,a2.size,a2.dtype)

#2d
a3=np.array([[1,2,3],[3.5,"k",2]])
print(a3)
print(a3.ndim,a3.shape,a3.size,a3.dtype)

#3d

a4=np.array([[[1,2,3],[3.5,"k",2]],[[50,60,70],[70,80,20]],[[1,2,3],[1,2,3]]])
print(a4)
print(a4.ndim,a4.shape,a4.size,a4.dtype)
print(a4[1,1,1])

#output
0
2
[1.  2.  3.3]
1 (3,) 3 float64
[['1' '2' '3']
 ['3.5' 'k' '2']]
2 (2, 3) 6 <U32
[[['1' '2' '3']
  ['3.5' 'k' '2']]

 [['50' '60' '70']
  ['70' '80' '20']]

 [['1' '2' '3']
  ['1' '2' '3']]]
3 (3, 2, 3) 18 <U32
80
'''

#other ways to create array
'''
a1=np.array([[1,2,3],[4,5,6]],dtype=str)#dtyep=str   bool int float
print("\n",a1)
a2=np.zeros((3,2))
print("\n",a2)
a2=np.ones((3,2,2))
print("\n",a2)
a3=np.eye((3))
print("\n",a3)
a4=a1.transpose()
print("\n",a4)
a5=np.arange(1,11,2)
print("\n",a5)


a=np.array([[90,40,25],[98,35,20]])
print("\n",a)
a.sort()
print("\n",a)
a.sort(axis=0)
print("\n",a)
print("\nmax in array= ",a.max())
print("\nmax in rows= ",a.max(axis=1))
print("\nmax in clos= ",a.max(axis=0))
a6=np.array([1,2,3],ndmin=3)
print("\n",a6,a6.ndim)
print("\nsum in array= ",a.sum())
print("\nsum in rows= ",a.sum(axis=1))
print("\nsum in clos= ",a.sum(axis=0))
print("\nstd in array= ",a.std())
print("\nstd in rows= ",a.std(axis=1))
print("\nstd in clos= ",a.std(axis=0))
a7=np.array([1,2,3,4,5,6])
print(a7.reshape(2,3))
print("\n",a7)


#output


 [['1' '2' '3']
 ['4' '5' '6']]

 [[0. 0.]
 [0. 0.]
 [0. 0.]]

 [[[1. 1.]
  [1. 1.]]

 [[1. 1.]
  [1. 1.]]

 [[1. 1.]
  [1. 1.]]]

 [[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]

 [['1' '4']
 ['2' '5']
 ['3' '6']]

 [1 3 5 7 9]

 [[90 40 25]
 [98 35 20]]

 [[25 40 90]
 [20 35 98]]

 [[20 35 90]
 [25 40 98]]

max in array=  98

max in rows=  [90 98]

max in clos=  [25 40 98]

 [[[1 2 3]]] 3

sum in array=  308

sum in rows=  [145 163]

sum in clos=  [ 45  75 188]

std in array=  30.93900810016737

std in rows=  [30.09245014 31.47838765]

std in clos=  [2.5 2.5 4. ]
[[1 2 3]
 [4 5 6]]

 [1 2 3 4 5 6]
 '''
#arithmatic operations

b=np.array([[1,2,3],[4,5,6]])
a=np.array([[1,2,3],[4,5,6]])
print(a+b)
print(a-b)
print(a*b)
print(a%b)
print(a/b)
print(a//b)
print(a**3)
#print(a@b) error
c=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a@c)
'''
#output

[[ 2  4  6]
 [ 8 10 12]]
[[0 0 0]
 [0 0 0]]
[[ 1  4  9]
 [16 25 36]]
[[0 0 0]
 [0 0 0]]
[[1. 1. 1.]
 [1. 1. 1.]]
[[  1   8  27]
 [ 64 125 216]]
[[30 36 42]
 [66 81 96]]
 '''