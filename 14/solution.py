def parse_line(input_line):
    # takes a string of coordinates and converts into to a list of tuple pair ints
    coords_list = []
    coords_string_list = input_line.split(' -> ')
    for coords_string in coords_string_list:
        x, y = coords_string.split(',')
        coords_list.append((int(x), int(y)))
    return coords_list

def solution(inputarray):
    # initialise a 2 dimensional array of . (empty) and # (occupied)
    # start with empty 2d array first

    cave = [['.' for x in range(600)] for y in range(600)]
    # then fill in the cave with the input
    for line in inputarray:
        path = parse_line(line)
        for i in range(len(path) - 1):
            start, end = path[i], path[i+1]
            # if path is horizontal
            if start[1] == end[1]:
                if start[0] < end[0]:
                    for x in range(start[0], end[0] + 1, 1):
                        cave[start[1]][x] = '#'
                else:
                    for x in range(start[0], end[0] - 1, -1):
                        cave[start[1]][x] = '#'
            # if path is vertical
            if start[0] == end[0]:
                if start[1] < end[1]:
                    for y in range(start[1], end[1] + 1):
                        cave[y][start[0]] = '#'
                else:
                    for y in range(start[1], end[1] - 1, -1):
                        cave[y][start[0]] = '#'

    # start simulating sand motion
    # sand will fall down until it hits a wall or another sand particle
    # sand will move left or right until it hits a wall or another sand particle
    # sand will stop moving if it hits a wall or another sand particle and all three spaces below are filled

    resting_sand_count = 0
    fallen_sand = False

    while not fallen_sand:
        x = 500
        for y in range(500):
            if y == 499:
                fallen_sand = True
            if cave[y + 1][x] == '.':
                continue
            elif x > 0 and cave[y + 1][x - 1] == '.':
                x -= 1
                continue
            elif cave[y + 1][x + 1] == '.':
                x += 1
                continue
            else:
                cave[y][x] = 'o'
                resting_sand_count += 1
                break



    # for row in cave:
    #     for col in row:
    #         print(col, end='')
    #     print('')

    return resting_sand_count

    pass

def solution2(inputarray):
    # get max
    max_y = 0
    parsed_array = []
    for line in inputarray:
        parsed_line = parse_line(line)
        parsed_array.append(parsed_line)
        for coords in parsed_line:
            max_y = max(max_y, coords[1])

    cave = [['.' for x in range(800)] for y in range(max_y+ 2)]

    for path in parsed_array:
        for i in range(len(path) - 1):
            start, end = path[i], path[i+1]
            # if path is horizontal
            if start[1] == end[1]:
                if start[0] < end[0]:
                    for x in range(start[0], end[0] + 1, 1):
                        cave[start[1]][x] = '#'
                else:
                    for x in range(start[0], end[0] - 1, -1):
                        cave[start[1]][x] = '#'
            # if path is vertical
            if start[0] == end[0]:
                if start[1] < end[1]:
                    for y in range(start[1], end[1] + 1):
                        cave[y][start[0]] = '#'
                else:
                    for y in range(start[1], end[1] - 1, -1):
                        cave[y][start[0]] = '#'

    # start simulating sand motion
    # sand will fall down until it hits a wall or another sand particle
    # sand will move left or right until it hits a wall or another sand particle
    # sand will stop moving if it hits a wall or another sand particle and all three spaces below are filled

    resting_sand_count = 0
    stopped_sand = False

    while not stopped_sand:
        x = 500
        for y in range(len(cave)):
            if y == len(cave) - 1:
                cave[y][x] = 'o'
                resting_sand_count += 1
                continue
            if cave[y + 1][x] == '.':
                continue
            elif x > 0 and cave[y + 1][x - 1] == '.':
                x -= 1
                continue
            elif cave[y + 1][x + 1] == '.':
                x += 1
                continue
            else:
                if y == 0:
                    stopped_sand = True
                cave[y][x] = 'o'
                resting_sand_count += 1
                break

    # for row in cave:
    #     for col in row:
    #         print(col, end='')
    #     print('')

    return resting_sand_count


if __name__ == '__main__':
    f = open('input.txt', 'r')

    inputarray = f.read().splitlines()

    print(solution(inputarray))
    print(solution2(inputarray))
