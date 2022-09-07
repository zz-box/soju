
# 거스름돈으로 사용되는 500, 100, 50, 10 원 동전이 무수히 존재한다.
# 거슬러 줘야 할 돈이 1260원일 때, 거슬러 줘야 할 동전의 최소 개수를 구하여라

n = 1260
coin_list = [500, 100, 50, 10]
cnt = 0

for coin in coin_list:
    cnt += n // coin
    n %= coin

print (cnt)