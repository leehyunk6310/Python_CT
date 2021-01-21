def binary_serach(array, target, start, end):
    if start > end:
        return None
    mid = (start+end) // 2
    if target == array[mid]:
        return mid
    elif target < array[mid]:
        binary_serach(array, target, start, mid-1)
    else:
        binary_serach(array, target, mid+1, end)


n = int(input())
array = list(map(int,input().split()))
array.sort()

m = int(input())
x = list(map(int,input().split()))

for i in x:
    result = binary_serach(array, i, 0, n-1)
    print(i)
    if result != None:
        print("yes", end = " ")
    else:
        print("no", end = " ")