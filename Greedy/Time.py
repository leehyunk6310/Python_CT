n = input()
n = int(n)
count = 0

for h in range(n+1):
    for m in range(60):
        for s in range(60):
            if str(n) in str(h) + str(m) + str(s):  #�� �ð��ȿ� n�� ������� ī��Ʈ
                count += 1
        

print(count)