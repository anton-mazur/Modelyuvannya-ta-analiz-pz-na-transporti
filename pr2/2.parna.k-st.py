def parni(massiv):
    for number in massiv:
        digits = len(str(number))
        parity = "парна" if digits % 2 == 0 else "непарна"

        last = digits % 10
        if last == 1:
            word = "цифру"
        elif last in (2, 3, 4):
            word = "цифри"
        else:
            word = "цифр"

        print(f"{number} містить {digits} {word} ({parity} кількість цифр)")


if __name__ == "__main__":
    numbs = []
    print("Please, type in number <100000 (0 for exit)")
    while len(numbs) < 500:
        try:
            i = int(input())
        except ValueError:
            print("Wrong!")
            continue
        if i == 0:
            print("Exiting...")
            break
        if i < 0 or i >= 100000:
            print("Wrong!")
        else:
            numbs.append(i)
    parni(numbs)