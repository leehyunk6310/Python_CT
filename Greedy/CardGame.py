row, column = map(int, input().split())

arr_card = []

for i in range(row):
        arr = list(map(int, input().split()))   
        arr_card.append(arr)        #������ �迭�� ����

minVal = min(arr_card[0])           #�迭�� ù��° ����Ʈ �� �ּҰ����� �ʱ�ȭ
for i in range(row):
    if(minVal < min(arr_card[i])):
        minVal = min(arr_card[i])   #minVal ����

print(minVal)