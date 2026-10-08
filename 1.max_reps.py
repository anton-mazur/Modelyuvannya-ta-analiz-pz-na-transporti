def max_reps(massive):
    max_count = 0
    current_count = 0
    for element in massive:
        if element == 1:
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0
    return max_count




if __name__ =="__main__":
    numbs = []
    print("Please, type in 0 or 1 (2 for exit)")
    while len(numbs) < 100000:
        i = int(input())
        if i == 2:
            print("Exiting...")
            break
        if i != 0 and i !=1:
            print("Wrong!")
        else:
            numbs.append(i)
    print(max_reps(numbs))