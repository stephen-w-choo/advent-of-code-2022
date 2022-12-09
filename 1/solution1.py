
def solution(array):
    max_val = [0, 0, 0]
    current_total = 0

    def get_max_3(val):
        if val > max_val[0]:
            max_val[0] = val
            if val > max_val[1]:
                max_val[0], max_val[1] = max_val[1], val
                if val > max_val[2]:
                    max_val[1], max_val[2] = max_val[2], val

    for line in array:
        if not line:
            get_max_3(current_total)
            current_total = 0
            continue
        current_total += line
    
    get_max_3(current_total)

    return sum(max_val)


if __name__ == '__main__':
    f = open('input.txt', 'r')

    array = []

    for line in f:
        try:
            array.append(int(line))
        except:
            array.append(None)

    print(solution(array))