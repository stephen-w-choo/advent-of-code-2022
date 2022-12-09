import re

CRATE_STATE = {}

def set_crate_state():
    global CRATE_STATE
    CRATE_STATE = {
        1: ['V', 'C', 'D', 'R', 'Z', 'G', 'B', 'W'],
        2: ['G', 'W', 'F', 'C', 'B', 'S', 'T', 'V'],
        3: ['C', 'B', 'S', 'N', 'W'],
        4: ['Q', 'G', 'M', 'N', 'J', 'V', 'C', 'P'],
        5: ['T', 'S', 'L', 'F', 'D', 'H', 'B'],
        6: ['J', 'V', 'T', 'W', 'M', 'N'],
        7: ['P', 'F', 'L', 'C', 'S', 'T', 'G'],
        8: ['B', 'D', 'Z'],
        9: ['M', 'N', 'Z', 'W'],
    }

def set_test_crate_state():
    global CRATE_STATE
    CRATE_STATE = {
        1: ['Z', 'N'],
        2: ['M', 'C', 'D'],
        3: ['P']
    }

def get_digits(inputstring):
    # takes a string and returns a list of integers
    digits = re.findall(r'\d+', inputstring)
    digits = map(int, digits)
    return list(digits)

def move_box1(instructions):
    # takes a list of 3 digits and makes the movements in the global state
    n_boxes, origin, destination = instructions

    for i in range(n_boxes):
        # move the box from the origin to the destination
        CRATE_STATE[destination].append(CRATE_STATE[origin].pop())

def move_box2(instructions):
    # takes a list of 3 digits and makes the movements in the global state
    print(CRATE_STATE)
    print(instructions)
    
    n_boxes, origin, destination = instructions
    stack = []
    for i in range(n_boxes):
        # pop the boxes from the origin and store in a stack
        stack.append(CRATE_STATE[origin].pop())
    while stack:
        CRATE_STATE[destination].append(stack.pop())

def solution1(inputarray):
    set_crate_state()
    for line in inputarray:
        instructions = get_digits(line)
        move_box1(instructions)

    res = []

    for CRATE in CRATE_STATE:
        res.append(CRATE_STATE[CRATE][-1])

    return res

def solution2(inputarray):
    set_crate_state()
    for line in inputarray:
        # convert the input array into a tuple of intervals
        instructions = get_digits(line)
        move_box2(instructions)

    res = []

    for CRATE in CRATE_STATE:
        res.append(CRATE_STATE[CRATE][-1])

    return res


if __name__ == '__main__':
    f = open('input.txt', 'r')
    
    inputarray = f.read().splitlines() 
    print(solution2(inputarray))
