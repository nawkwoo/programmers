import sys
input = sys.stdin.readline

n = int(input().strip())

low, high = 0, int(n**0.5) + 2

while low < high:
    mid = (low + high) // 2
    if mid * mid >= n:
        high = mid
    else:
        low = mid + 1

print(low)