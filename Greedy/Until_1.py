n, k = map(int, input().split())    #n�� 1�� �ɶ����� k�� �����ų�, n -=1�� �ϴ� �ڵ�
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