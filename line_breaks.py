def main():
    n, m = input().split(" ")
    n, m = int(n), int(m)

    words = []
    for _ in range(n):
        words.append(input())

    remaining_lines = m
    number_of_words = 0

    while remaining_lines and len(words) > 0:
        word = words.pop(0)
        if len(word) <= remaining_lines:
            number_of_words += 1
            remaining_lines -= len(word)
        else:
            break

    print(number_of_words)


for i in range(int(input())):
    main()
