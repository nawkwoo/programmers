n = int(input())

prev, curr = 1, 2

for _ in range(3, n + 1):
    prev, curr = curr, (prev + curr) % 15746

print(curr if n > 1 else prev)