import sys
input = sys.stdin.readline

N = int(input().strip())
sanggeun_cards = set(map(int, input().split()))
M = int(input().strip())
query_cards = list(map(int, input().split()))

results = [1 if card in sanggeun_cards else 0 for card in query_cards]

sys.stdout.write(" ".join(map(str, results)) + "\n")