n = int(input())
count = 0
for _ in range(n):
    s = input().split()
    c = 0
    for i in s:
        if i == "1":
            c += 1
    if c >= 2:
        count += 1

print(count)
