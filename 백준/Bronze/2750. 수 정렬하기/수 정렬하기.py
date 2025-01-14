import sys
input = sys.stdin.readline

N = int(input().strip())
numbers = [int(input().strip()) for _ in range(N)]

numbers.sort()

for num in numbers:
    print(num)