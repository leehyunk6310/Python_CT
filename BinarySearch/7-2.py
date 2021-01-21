def binary_serach(array, target, start, end):
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        binary_serach(array, target, start, mid - 1)
    else:
        binary_serach(array, target, mid+1, end)



n , target = list(map(int, input().split()))
array = list(map(int ,input().split()))

result = binary_serach(array, target, 0, n-1)
if result == None:
    print("Not exist!")
else:
    print(result + 1)