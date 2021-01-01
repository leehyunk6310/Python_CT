n, k = map(int, input().split())    #n이 1이 될때까지 k로 나누거나, n -=1을 하는 코드
count = 0

while(True):
    if n == 1:
        break

    if n%k == 0:
        n /= k
        count += 1
    else:
        n -= 1
        count += 1

print(count)