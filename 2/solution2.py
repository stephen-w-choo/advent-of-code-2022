
A_MOVE = ["A", "B", "C"] # opponent's moves - rock paper scissors
B_MOVE = ["X", "Y", "Z"] # your moves - rock paper scissors

def rps_move(a_index, b_outcome):
    # takes index of first move and the outcome required, with 
    # 0 representing a loss, 1 representing a draw and 2 representing a win
    # uses modulo 3 to wrap around and get the result
    
    move_required = (a_index + (b_outcome - 1) + 3) % 3

    if b_outcome == 0: # loss
        return move_required + 1
    if b_outcome == 1: # draw
        return move_required + 1 + 3

    return move_required + 1 + 6 # win

def outcome_cache():
    # creates a cache of all possible outcomes
    # this is used to avoid having to calculate the outcome
    # of every possible combination of moves
    cache = {}
    for index1, move1 in enumerate(A_MOVE):
        for index2, move2 in enumerate(B_MOVE):
            cache[f"{move1} {move2}"] = rps_move(index1, index2)
    return cache

# created cache

CACHE = {
    'A X': 3, 
    'A Y': 4, 
    'A Z': 8, 
    'B X': 1, 
    'B Y': 5, 
    'B Z': 9, 
    'C X': 2, 
    'C Y': 6, 
    'C Z': 7
    }

def solution(array):
    res = 0
    for line in array:
        res += CACHE[line]
    
    return res

if __name__ == '__main__':
    f = open('input.txt', 'r')

    array = []

    for line in f:
        try:
            array.append(str(line[:3]))
        except:
            array.append(None)

    print(solution(array))