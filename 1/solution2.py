
def solution(array):
    res = 0
    # Your code here
    current_total = sum(array[0:2])
    next_total = sum(array[1:3])
    for i in range(len(array) - 3):
        if next_total > current_total:
            res += 1
        current_total = next_total
        next_total = next_total - array[i] + array[i+3]
    return res


if __name__ == '__main__':
    f = open('input.txt', 'r')

    array = []

    for line in f:
        array.append(int(line))

    print(solution(array))