import sys
from collections import deque

input = sys.stdin.readline

dq = deque()

results = []

N = int(input().strip())

for _ in range(N):
    command = input().strip()
    
    if command.startswith("1"):
        _, value = command.split()
        dq.appendleft(int(value))
    elif command.startswith("2"):
        _, value = command.split()
        dq.append(int(value))
    elif command == "3":
        if dq:
            results.append(dq.popleft())
        else:
            results.append(-1)
    elif command == "4":
        if dq:
            results.append(dq.pop())
        else:
            results.append(-1)
    elif command == "5":
        results.append(len(dq))
    elif command == "6":
        results.append(1 if not dq else 0)
    elif command == "7":
        if dq:
            results.append(dq[0])
        else:
            results.append(-1)
    elif command == "8":
        if dq:
            results.append(dq[-1])
        else:
            results.append(-1)

sys.stdout.write("\n".join(map(str, results)) + "\n")
