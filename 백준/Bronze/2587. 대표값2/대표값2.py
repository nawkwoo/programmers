import sys
input = sys.stdin.readline

numbers = [int(input().strip()) for _ in range(5)]
average = sum(numbers) // len(numbers)
sorted_numbers = sorted(numbers)
median = sorted_numbers[len(sorted_numbers) // 2]

print(average)
print(median)