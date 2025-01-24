# find the number that appears once and others twice:
# 0 xor num=num
# num xor num =0
#1 xor 2 xor 3 xor 3 xor 2=  (1)xor(2 xor 2)xor(3 xor 3)
#=> 1 xor 0 xor 0=1
def find_once(arr):
    XOR=0
    for num in arr:
        XOR=XOR^num
    return XOR
if __name__=="__main__":
    arr=list(map(int,input("Enter elements: ").split()))
    print(arr)
    num=find_once(arr)
    print("num is :",num)