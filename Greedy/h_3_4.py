

n, k = map(int, input().split())

n = 10
k = 3
cnt = 0

while n > 1:
    if n%k != 0:
        n -= 1
        cnt += 1

    elif n%k == 0:
        n = n/k
        cnt += 1

