n, m = map(int, input().split())
x, y, d = map(int, input().split())
geo = []
for i in range(n):
    geo.append(input().split())

x_move = [-1, 0, 1, 0]
y_move = [0, 1, 0, -1]

cnt = 0
for i in range(4):
    if d == i:
        if geo[x][y] == 0:
            x = x + x_move[i]
            geo[x][y] = 1
            cnt += 1
        else:
            d = 3



if d == 0:
    if geo[x][y] == 0:
        x -= 1
        geo[x][y] = 1
        cnt += 1
    else:
        d = 3
elif d == 1:
    if geo[x][y] == 0:
        y += 1
        geo[x][y] = 1
        cnt += 1
    else:
        d = 0
elif d == 2:
    if geo[x][y] == 0:
        x += 1
        geo[x][y] = 1
        cnt += 1
    else:
        d = 1
elif d == 3:
    if geo[x][y] == 0:
        y -= 1
        geo[x][y] = 1
        cnt += 1
    else:
        d = 2