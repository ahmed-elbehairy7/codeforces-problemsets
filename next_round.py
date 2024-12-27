def main():
    n, k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]

    m = a[k - 1]
    count = 0
    for i in range(n):
        if a[i] >= m and a[i] > 0:
            count += 1
        else:
            break

    print(count)


main()
