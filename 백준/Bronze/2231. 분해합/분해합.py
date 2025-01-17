import sys
input = sys.stdin.readline

def D_sum(x):
    return x + sum(map(int, str(x)))

N = int(input().strip())

result = 0
for candidate in range(max(1, N - len(str(N)) * 9), N):
    if D_sum(candidate) == N:
        result = candidate
        break

print(result)