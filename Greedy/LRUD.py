r, c = 1, 1
size = map(int,input())
move = input().split()

for i in move:
    if i == 'R':
        c += 1
    if i == 'L':
        c -= 1
    if i == 'U':
        r -= 1
    if i == 'D':
        r += 1    
    if c<1:
        c = 1
    if r<1:
        r = 1
    
print(r, c)