def main22():
    n = int(input())
    a = [int(x) for x in input().split(" ")]

    if (sum(a) / n) % 1:
        print("NO")
        return
    print("YES")


def main():
    n = int(input())
    a = [int(x) for x in input().split(" ")]

    median = sum(a) / n
    if median % 1:
        print("NO")
        return

    for i in [0, -3]:
        if ((a[i] + a[i + 2]) / 2) != median:
            print("NO")
            return

    print("YES")


for _ in range(int(input())):
    main()
