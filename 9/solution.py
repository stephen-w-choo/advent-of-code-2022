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
    # additional diagonal positions
    (2, 2): (1, 1),
    (-2, 2): (-1, 1),
    (2, -2): (1, -1),
    (-2, -2): (-1, -1),
}
# dictionary for parsing the head movement
head_movement = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, 1),
    'D': (0, -1),
}

def movement(direction, head_position):
    # takes a direction for a head  position and returns the new head position
    head_position = (head_position[0] + head_movement[direction][0], head_position[1] + head_movement[direction][1])
    return head_position

def update(head_position, follower_position):
    # takes a head and follower position and updates the follower positions
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
            head = movement(direction, head)
            head, tails = update(head, tails)
            tail_positions.add(tails)

    return len(tail_positions)

def solution2(inputarray):
    knots_length = 10
    knots = [(0, 0) for i in range(knots_length)]

    tail_positions = set([knots[-1]])

    for instruction in inputarray:
        direction, distance = instruction.split()
        distance = int(distance)
        for i in range(distance):
            knots[0] = movement(direction, knots[0])
            for j in range(knots_length - 1):
                knots[j], knots[j + 1] = update(knots[j], knots[j + 1])

            tail_positions.add(knots[-1])
    return len(tail_positions)

if __name__ == '__main__':
    f = open('input.txt', 'r')

    inputarray = f.read().splitlines()
    print(solution1(inputarray))
    print(solution2(inputarray))
