input_data = input()
row = int(input_data[1])
col = ord(input_data[0]) - ord('a') + 1 #ord�� ����Ͽ� ���ڷ� ��ȯ
num = 0

steps = [[-2, 1], [-2, -1], [2, 1], [2, -1], [1, 2], [-1, 2], [1, -2], [-1, -2]] #�̵������� ���

for i in steps:
    ncol, nrow = col + i[0], row + i[1] 
    if ncol > 0 and nrow > 0 and ncol < 9 and nrow < 9: #ü���� �ȿ� �ִ� ��츸
        num += 1

print(num)
    