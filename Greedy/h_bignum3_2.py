


n, m, k = map(int, input().split()) # n: 입력 갯수, m: 몇번 더해지는지, k: 더해지는 횟수
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

result = 0
counting = 1

while counting <= m:
    for j in range(k):
        
        counting += 1
        result += first
        