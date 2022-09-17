n = int(input())
moves = input().split()

way_list = ["R", "L", "U", "D"]
x_move = [0, 0, -1, 1]
y_move = [1, -1, 0, 0]

x, y = 1, 1
for move in moves:
    for i in range(4):
        if move == way_list[i]:
            dx = x + x_move[i]
            dy = y + y_move[i]
    if (dx < 1 or dx > n) or (dy<1 or dy>n):
        continue
    x = dx
    y = dy
print(x, y)