import sys
input = sys.stdin.readline

N, M = map(int, input().split())
cards = list(map(int, input().split()))

best_sum = 0

for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            total = cards[i] + cards[j] + cards[k]
            # M을 넘지 않고, M에 최대한 가까운 합을 갱신
            if total <= M and total > best_sum:
                best_sum = total

print(best_sum)