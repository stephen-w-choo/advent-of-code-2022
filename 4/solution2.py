def convert_to_interval_pair(inputstring):
    pair = inputstring.split(',')
    pair = map(lambda x: x.split('-'), pair)
    pair = map(lambda x: (int(x[0]), int(x[1])), pair)
    return list(pair)

def check_overlap(elf_pair):
    # check if the intervals overlap
    if elf_pair[0][0] <= elf_pair[1][1] and elf_pair[1][0] <= elf_pair[0][1]:
        return True
    return False

def solution(inputarray):
    overlaps = 0

    for line in inputarray:
        # convert the input array into a tuple of intervals
        elf_pair = convert_to_interval_pair(line)
        if check_overlap(elf_pair):
            overlaps += 1
        
    return overlaps


if __name__ == '__main__':
    f = open('input.txt', 'r')
    
    inputarray = f.read().splitlines() 
    print(solution(inputarray))
