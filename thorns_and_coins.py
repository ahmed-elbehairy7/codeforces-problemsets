def main():
    n: int = int(input())
    world = input()

    last_was_throne = False
    coins = 0

    for i in range(n):
        match (world[i]):
            case "*":
                if last_was_throne:
                    break
                last_was_throne = True
            case "@":
                coins += 1
                last_was_throne = False
            case _:
                last_was_throne = False

    print(coins)


for _ in range(int(input())):
    main()
