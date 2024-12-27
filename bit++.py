x = 0
n = int(input())
for _ in range(n):
    s = input()
    if s[0] == "+" or s[2] == "+":
        x += 1
    else:
        x -= 1
print(x)
