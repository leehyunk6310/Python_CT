n, m, k = map(int, input().split())
arr = list(map(int ,input().split()))
sum = 0
count = 0
arr.sort()
maxVal = arr[-1]        //최대값
bmaxVal = arr[-2]       //최대값 바로 아랫값

for i in range(m):
    if count != k:
        sum += maxVal
        
    else:
        sum += bmaxVal
        count = 0
    count += 1

print(sum)



