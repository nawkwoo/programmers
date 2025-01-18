import sys
input = sys.stdin.readline

stack = []

results = []

N = int(input().strip())

for _ in range(N):
    command = input().strip()
    
    if command.startswith("push"):
        _, value = command.split()
        stack.append(int(value))
    elif command == "pop":
        if stack:
            results.append(stack.pop())
        else:
            results.append(-1)
    elif command == "size":
        results.append(len(stack))
    elif command == "empty":
        results.append(1 if not stack else 0)
    elif command == "top":
        if stack:
            results.append(stack[-1])
        else:
            results.append(-1)

sys.stdout.write("\n".join(map(str, results)) + "\n")