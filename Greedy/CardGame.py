row, column = map(int, input().split())

arr_card = []

for i in range(row):
        arr = list(map(int, input().split()))   
        arr_card.append(arr)        #이차원 배열을 생성

minVal = min(arr_card[0])           #배열의 첫번째 리스트 중 최소값으로 초기화
for i in range(row):
    if(minVal < min(arr_card[i])):
        minVal = min(arr_card[i])   #minVal 갱신

print(minVal)