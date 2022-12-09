def solution1(input_string):
    # make a sliding window of size 4
    # maintain a frequency dictionary
    letters = {}
    for i in range(4):
        char = input_string[i]
        if char not in letters:
            letters[char] = 0
        letters[char] += 1

    for i in range(4, len(input_string)):
        # return i if the dictionary has 4 unique letters
        if len(letters) == 4:
            return i
        # add the char to the frequency dictionary
        newchar = input_string[i]
        if newchar not in letters:
            letters[newchar] = 0
        letters[newchar] += 1
        # remove the lastchar from the frequency dictionary
        lastchar = input_string[i - 4]
        letters[lastchar] -= 1
        if letters[lastchar] == 0:
            del letters[lastchar]
    
    return False

def solution2(input_string):
    # make a sliding window of size 14
    # maintain a frequency dictionary
    letters = {}
    for i in range(14):
        char = input_string[i]
        if char not in letters:
            letters[char] = 0
        letters[char] += 1

    for i in range(14, len(input_string)):
        # return i if the dictionary has 4 unique letters
        if len(letters) == 14:
            return i
        # add the char to the frequency dictionary
        newchar = input_string[i]
        if newchar not in letters:
            letters[newchar] = 0
        letters[newchar] += 1
        # remove the lastchar from the frequency dictionary
        lastchar = input_string[i - 14]
        letters[lastchar] -= 1
        if letters[lastchar] == 0:
            del letters[lastchar]
    
    return False


if __name__ == '__main__':
    f = open('input.txt', 'r')
    
    input_string = f.read()
    print(solution2(input_string))
