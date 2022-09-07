N, M, K = map(int, input().split())

num_list = list(map(int, input().split())) # 2 4 4 5 6

num_list.sort()

first = num_list[N-1]
second = num_list[N-2]

sum = (first * K + second)*(M//(K+1)) + first*(M%(K+1))
print(sum)