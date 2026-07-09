from collections import Counter

n = int(input())
shoes = Counter(map(int, input().split()))
m = int(input())

earned = 0
for _ in range(m):
    size, price = map(int, input().split())
    if shoes[size] > 0:
        earned += price
        shoes[size] -= 1

print(earned)