location = input()
x, y = location[0], int(location[1])

x_list = ['a', 'b' ,'c' ,'d' ,'e', 'f', 'g', 'h']
for i in range(8):
    if x == x_list[i]:
        x = i + 1

cnt =8 
if x<3 or x>6:
    cnt -=2
if x<2 or x>7:
    cnt -=1

if y<3 or y>6:
    cnt -=2
if y<2 or y>7:
    cnt -=1

print(cnt)