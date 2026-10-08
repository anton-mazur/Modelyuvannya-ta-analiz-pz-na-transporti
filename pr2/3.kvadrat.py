LIMIT = 10000
EXIT_VALUE = 10001


def sortkvadrat(numbs):
    return sorted(x**2 for x in numbs)


if __name__ == "__main__":
    numbs = []
    print(f"Введіть числа від -{LIMIT} до {LIMIT} ({EXIT_VALUE} для виходу)")
    while len(numbs) < LIMIT:
        try:
            i = int(input())
        except ValueError:
            print("Wrong!")
            continue
        if i == EXIT_VALUE:
            print("Exiting...")
            break
        if i < -LIMIT or i > LIMIT:
            print("Wrong!")
        else:
            numbs.append(i)
    print("Sorted by square:")
    print(sortkvadrat(numbs))