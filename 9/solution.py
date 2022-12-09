# dictionary that takes the difference in position between the head and the tail
# and returns the movement of the tail
tail_movement = {
    # cardinal positions
    (0, 2): (0, 1),
    (0, -2): (0, -1),
    (2, 0): (1, 0),
    (-2, 0): (-1, 0),
    # diagonal positions
    (1, 2): (1, 1),
    (2, 1): (1, 1),
    (-1, 2): (-1, 1),
    (-2, 1): (-1, 1),
    (1, -2): (1, -1),
    (2, -1): (1, -1),
    (-1, -2): (-1, -1),
    (-2, -1): (-1, -1),
}
# dictionary for parsing the head movement
head_movement = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, 1),
    'D': (0, -1),
}

def movement(direction, head_position, follower_position):
    # takes a direction for a head and follower position and returns the new head and follower positions
    head_position = (head_position[0] + head_movement[direction][0], head_position[1] + head_movement[direction][1])
    position_difference = (head_position[0] - follower_position[0], head_position[1] - follower_position[1])
    if position_difference in tail_movement:
        follower_position = (follower_position[0] + tail_movement[position_difference][0], follower_position[1] + tail_movement[position_difference][1])
    
    return head_position, follower_position

def solution1(inputarray):
    head = (0, 0)
    tails = (0, 0)

    tail_positions = set([tails])

    for instruction in inputarray:
        direction, distance = instruction.split()
        distance = int(distance)
        for i in range(distance):
            head = (head[0] + head_movement[direction][0], head[1] + head_movement[direction][1])
            position_difference = (head[0] - tails[0], head[1] - tails[1])
            if position_difference in tail_movement:
                tails = (tails[0] + tail_movement[position_difference][0], tails[1] + tail_movement[position_difference][1])
                tail_positions.add(tails)
    
    return len(tail_positions)

def solution2(inputarray):
    pass
            
if __name__ == '__main__':
    f = open('input.txt', 'r')
    
    inputarray = f.read().splitlines() 
    print(solution1(inputarray))
    print(solution2(inputarray))
