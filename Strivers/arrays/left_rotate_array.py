#left rotate array by k place
def left_rotate(arr,k):
    n=len(arr)
    k=k%n
    rotated_arr=arr[k::]+arr[0:k:]
    print(rotated_arr)
if __name__=="__main__":
    arr=list(map(int,input("Enter elements: ").split()))
    print(arr)
    k=int(input("no of rotations: "))
    left_rotate(arr,k)