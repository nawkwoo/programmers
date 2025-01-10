import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))

min1 = min(numbers)
max1 = max(numbers)

print(min1, max1)