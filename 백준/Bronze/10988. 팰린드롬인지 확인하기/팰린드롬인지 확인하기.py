word = input().strip()
length = len(word)
is_palindrome = True

for i in range(length // 2):
    if word[i] != word[length - 1 - i]:
        is_palindrome = False
        break

print(1 if is_palindrome else 0)