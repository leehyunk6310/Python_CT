n, m = map(int, input().split())    #행 열

d = [[0] * m for _ in range(n)]     #방문 위치 저장

x, y, direction = map(int, input().split()) #현재 위치, 방향
d[x][y] = 1

arr = []  
for i in range(n):
    arr.append(list(map(int, input().split())))   #대륙과 바다 표시

dx = [-1, 0, 1, 0]  #0 - 북 //  1 - 동 //  2 - 남 // 3 - 서
dy = [0, 1, 0, -1]  

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction =3

count = 1
turn_time = 0

while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if d[nx][ny] == 0 and arr[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    
    else:
        turn_time += 1

    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if arr[nx][ny] == 0:
            x,y = nx, ny 
        else:
            break
        turn_time = 0    

print(count)