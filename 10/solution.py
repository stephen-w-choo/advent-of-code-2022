from collections import deque 
# dictionary that takes the difference in position between the head and the tail
# and returns the movement of the tail

def load_register(inputarray):
    # takes an array and loads it into a register queue, returns the register
    register = deque()
    for line in inputarray:
        register.appendleft(None)
        if line != "noop":
            addx = line.split()
            register.appendleft(int(addx[1]))
    return register
        

def solution1(inputarray):
    pass

    # initialise a queue
    
    register = load_register(inputarray)
    
    register_value = 1
    xth_cycle = 1
    signal_strengths = []

    while register:
        if (xth_cycle + 20) % 40 == 0:
            print(xth_cycle, register_value)
            signal_strengths.append((xth_cycle) * register_value)
        cycle_end = register.pop()
        if cycle_end:
            register_value += cycle_end
        xth_cycle += 1

    return sum(signal_strengths)

def solution2(inputarray):
    # CRT screen is 40x6
    # leftmost pixel is 0, rightmost is 39
    # current pixel position can de determined by the cycle number

    # at the end of each cycle, check if the pixel position % 40 overlaps with range (register_value - 1, register_value + 2)
    register = load_register(inputarray)
    
    register_value = 1
    xth_cycle = 0


    while register:
        if (xth_cycle) % 40 in range(register_value - 1, register_value + 2):
            print('#', end="")
        else:
            print('.', end="")
        cycle_end = register.pop()
        if cycle_end:
            register_value += cycle_end
        xth_cycle += 1
        if (xth_cycle) % 40 == 0:
            print()


if __name__ == '__main__':
    f = open('input.txt', 'r')

    inputarray = f.read().splitlines()
    print(solution1(inputarray))
    print(solution2(inputarray))
