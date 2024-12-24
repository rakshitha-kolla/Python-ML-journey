'''
Tower of Hanoi is a mathematical puzzle where we have three rods (A, B, and C) and N disks. Initially, all the disks are stacked in decreasing value of diameter i.e., the smallest disk is placed on the top and they are on rod A. The objective of the puzzle is to move the entire stack to another rod (here considered C), obeying the following simple rules:

    Only one disk can be moved at a time.
    Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack i.e. a disk can only be moved if it is the uppermost disk on a stack.
    No disk may be placed on top of a smaller disk.
'''
def tower_of_hanoi(n,from_rod,to_rod,aux_rod):
	if n==0:
		return
	tower_of_hanoi(n-1,from_rod,aux_rod,to_rod)
	print("move disk",n,"from rod",from_rod,"to rod",to_rod)
	tower_of_hanoi(n-1,aux_rod,to_rod,from_rod)
n=int(input("Enter no of disks: "))
tower_of_hanoi(n,"A","C","B")
            
