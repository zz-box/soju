n, m = map(int, input().split())
first_row = list(map(int, input().split()))
second_row = list(map(int, input().split()))
third_row = list(map(int, input().split()))

first_row.sort()
second_row.sort()
third_row.sort()

min_list = [first_row[0], second_row[0], third_row[0]]

min_list.sort()

print(min_list[n-1])

# min()함수를 이용해서도 풀어보기