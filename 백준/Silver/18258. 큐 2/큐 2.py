import sys
from collections import deque

input = sys.stdin.readline

queue = deque()

results = []

N = int(input().strip())

for _ in range(N):
    command = input().strip()
    
    if command.startswith("push"):
        _, value = command.split()
        queue.append(int(value))
    elif command == "pop":
        if queue:
            results.append(queue.popleft())
        else:
            results.append(-1)
    elif command == "size":
        results.append(len(queue))
    elif command == "empty":
        results.append(1 if not queue else 0)
    elif command == "front":
        if queue:
            results.append(queue[0])
        else:
            results.append(-1)
    elif command == "back":
        if queue:
            results.append(queue[-1])
        else:
            results.append(-1)

sys.stdout.write("\n".join(map(str, results)) + "\n")
