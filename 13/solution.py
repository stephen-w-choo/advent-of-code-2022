from functools import cmp_to_key
import json

def compare_lists(a, b):
    # takes two lists and compares the individual elements
    for i in range(min(len(a), len(b))):
        if type(a[i]) == int and type(b[i]) == int:
            if a[i] < b[i]:
                return -1
            if a[i] > b[i]:
                return 1
            if a[i] == b[i]:
                continue
            # continues if the elements are equal
        # if the elements are lists or mixed, convert to lists and repeat comparison
        if type(a[i]) == list or type(b[i]) == list:
            a_element = a[i]
            b_element = b[i]
            if type(a[i]) == int:
                a_element = [a[i]]
            if type(b[i]) == int:
                b_element = [b[i]]
            comparison = compare_lists(a_element, b_element)
            if comparison < 0:
                return -1
            if comparison > 0:
                return 1
            if comparison == 0:
                continue
    
    # if lists are exhausted, compare the list lengths
    if len(a) < len(b):
        return -1
    if len(a) > len(b):
        return 1
    
    # if lists are equal
    return 0

def convert_to_pairs(inputarray):
    # takes an array of strings and returns an array of tuples
    outputarray = []
    for i in range(0, len(inputarray), 3):
        outputarray.append((json.loads(inputarray[i]), json.loads(inputarray[i+1])))
    return outputarray

def convert_to_single_lists(inputarray):
    # takes an array of strings and returns an array of lists
    outputarray = []
    for i in range(0, len(inputarray), 3):
        outputarray.append(json.loads(inputarray[i]))
        outputarray.append(json.loads(inputarray[i+1]))
    return outputarray

def solution(inputarray):
    # parse input array
    inputarray = convert_to_pairs(inputarray)

    index_count = 0

    for index, pair in enumerate(inputarray):
        a, b = pair
        if compare_lists(a, b) < 0:
            index_count += index + 1
    
    return index_count

def solution2(inputarray):
    # parse input array
    inputarray = convert_to_single_lists(inputarray)
    inputarray.append([[2]])
    inputarray.append([[6]])
    inputarray.sort(key=cmp_to_key(compare_lists))

    for index, packet in enumerate(inputarray):
        if packet == [[2]]:
            index1 = index + 1
        if packet == [[6]]:
            index2 = index + 1

    return index1 * index2


if __name__ == '__main__':
    f = open('input.txt', 'r')

    inputarray = f.read().splitlines()

    print(solution(inputarray))
    print(solution2(inputarray))
