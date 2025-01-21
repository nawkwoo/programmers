import sys
input = sys.stdin.readline

# 출입 기록 수 입력
n = int(input().strip())

# 출입 기록 저장 딕셔너리
log = {}

# 로그 처리
for _ in range(n):
    name, action = input().strip().split()
    if action == "enter":
        log[name] = True  # 회사에 들어옴
    elif action == "leave":
        if name in log:
            del log[name]  # 회사에서 나감

# 현재 회사에 있는 사람의 이름 정렬 (사전 순 역순)
result = sorted(log.keys(), reverse=True)

# 결과 출력
sys.stdout.write("\n".join(result) + "\n")
