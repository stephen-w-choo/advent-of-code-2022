def item_value(item):
    if item.isupper():
        return ord(item) - 38
    if item.islower():
        return ord(item) - 96

def get_common_item(string1, string2, string3):
    string1set = set(string1)
    string2set = set(string2)
    string3set = set(string3)
    common_item = string1set.intersection(string2set, string3set).pop()
    return common_item


def solution(inputarray):
    res = 0

    for count, rucksack in enumerate(inputarray):
        # initialise count to keep track of triplets
        # variables to store the first, second and third strings
        if count % 3 == 0:
            first = rucksack
            continue
        if count % 3 == 1:
            second = rucksack
            continue
        if count % 3 == 2:
            third = rucksack
            common_item = get_common_item(first, second, third)
            res += item_value(common_item)
    
    return res


if __name__ == '__main__':
    f = open('input.txt', 'r')
    inputarray = f.read().splitlines() 

    print(solution(inputarray))
