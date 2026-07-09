A = set(input().split())
n = int(input())
result = True
for _ in range(n):
    s = set(input().split())
    if not (A > s):
        result = False
print(result)