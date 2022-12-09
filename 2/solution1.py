
A_MOVE = ["A", "B", "C"] # opponent's moves - rock paper scissors
B_MOVE = ["X", "Y", "Z"] # your moves - rock paper scissors

def rps_outcome(a_index, b_index):
    # takes indices of rock paper scissors moves
    # uses modulo 3 to wrap around and get the result
    
    res = ((a_index - b_index) + 3) % 3
    print(res)
    if res == 0: # tie
        return 3
    if res == 1: # b_index wins
        return 0

    return 6 # a_index wins

def outcome_cache():
    # creates a cache of all possible outcomes
    # this is used to avoid having to calculate the outcome
    # of every possible combination of moves
    cache = {}
    for index1, move1 in enumerate(A_MOVE):
        for index2, move2 in enumerate(B_MOVE):
            cache[f"{move1} {move2}"] = rps_outcome(index1, index2) + index2 + 1
    return cache

# created cache

CACHE = {
    'A X': 4, 
    'A Y': 8, 
    'A Z': 3, 
    'B X': 1, 
    'B Y': 5, 
    'B Z': 9, 
    'C X': 7, 
    'C Y': 2, 
    'C Z': 6
    }

def solution(array):
    res = 0
    for line in array:
        res += CACHE[line]
    
    return res

if __name__ == '__main__':
    f = open('input1.txt', 'r')

    array = []

    for line in f:
        try:
            array.append(str(line[:3]))
        except:
            array.append(None)

    print(solution(array))