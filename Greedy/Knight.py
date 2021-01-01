input_data = input()
row = int(input_data[1])
col = ord(input_data[0]) - ord('a') + 1 #ord를 사용하여 숫자로 변환
num = 0

steps = [[-2, 1], [-2, -1], [2, 1], [2, -1], [1, 2], [-1, 2], [1, -2], [-1, -2]] #이동가능한 경로

for i in steps:
    ncol, nrow = col + i[0], row + i[1] 
    if ncol > 0 and nrow > 0 and ncol < 9 and nrow < 9: #체스판 안에 있는 경우만
        num += 1

print(num)
    