n, m = map(int, input().split())

cnt = 0
while n >= m:
    if n % m == 0:
        n = n//m
        cnt += 1
    else:
        n -= 1
        cnt += 1

if n > 1:
    cnt += (n - 1)

print(cnt)