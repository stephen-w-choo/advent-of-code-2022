def item_value(item):
    if item.isupper():
        return ord(item) - 38
    if item.islower():
        return ord(item) - 96

def get_common_item(string1, string2):
    string1set = set(string1)
    string2set = set(string2)
    common_item = string1set.intersection(string2set).pop()
    return common_item


def solution(inputarray):
    res = 0

    for rucksack in inputarray:
        # split each line down the middle
        first = rucksack[len(rucksack)//2:] 
        second = rucksack[:len(rucksack)//2]

        # get the common item
        common_item = get_common_item(first, second)

        # add the item value to the total
        res += item_value(common_item)
    
    return res


if __name__ == '__main__':
    f = open('input.txt', 'r')
    
    inputarray = f.read().splitlines() 
    print(inputarray)
    print(solution(inputarray))
