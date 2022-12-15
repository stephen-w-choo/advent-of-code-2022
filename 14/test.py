def test(inputarray):
    count = 0
    for line in inputarray:
        for char in line:
            if char == 'o':
                count += 1
    return count

if __name__ == '__main__':
    f = open('test.txt', 'r')

    inputarray = f.read().splitlines()

    print(test(inputarray))
    # print(solution2(inputarray))
