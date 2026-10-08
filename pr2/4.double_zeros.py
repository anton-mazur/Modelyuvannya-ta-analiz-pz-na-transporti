def double_zeros(numbs):
    result = []
    for n in numbs:
        result.append(n)
        if n == 0:
            result.append(0)
    return result[:len(numbs)]



if __name__ == "__main__":
    numbs = []
    print("Please, type in number 0-9 (-1 for exit)")
    while len(numbs) < 10000:
        try:
            i = int(input())
        except ValueError:
            print("Wrong!")
            continue
        if i == -1:
            print("Exiting...")
            break
        if i < -1 or i >= 10:
            print("Wrong!")
        else:
            numbs.append(i)
    print(double_zeros(numbs))