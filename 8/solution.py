

def convert_to_grid(inputarray):
    # takes an array of strings and converts it to a grid
    res = []

    for line in inputarray:
        row = []
        for char in line:
            row.append(int(char))
        res.append(row)

    return res

def generate_empty_grid(length, width):
    res = [[0 for j in range(width)] for i in range(length)]

    return res


def solution1(inputarray):
    grid = convert_to_grid(inputarray)
    trees = set() # maintain a set of trees, identified by their coordinates

    LENGTH = len(grid)
    WIDTH = len(grid[0])

    # iterate through the grid downwards
    for x in range(WIDTH):
        for y in range(LENGTH):
            if y <= 0:
                trees.add((x, y))
                highest = grid[y][x]
            if highest < grid[y][x]:
                trees.add((x, y))
                highest = grid[y][x]
    
    # iterate through the grid rightwards
    for y in range(LENGTH):
        for x in range(WIDTH):
            if x <= 0:
                trees.add((x, y))
                highest = grid[y][x]
            if highest < grid[y][x]:
                trees.add((x, y))
                highest = grid[y][x]
    
    # iterate through the grid upwards
    for x in range(WIDTH):
        for y in range(LENGTH - 1, -1, -1):
            if y >= LENGTH - 1:
                trees.add((x, y))
                highest = grid[y][x]
            if highest < grid[y][x]:
                trees.add((x, y))
                highest = grid[y][x]
    
    # iterate through the grid leftwards
    for y in range(LENGTH):
        for x in range(WIDTH - 1, -1, -1):
            if x >= WIDTH - 1:
                trees.add((x, y))
                highest = grid[y][x]
            if highest < grid[y][x]:
                trees.add((x, y))
                highest = grid[y][x]

    return len(trees)


def solution2(inputarray):
    grid = convert_to_grid(inputarray)
    
    LENGTH = len(grid)
    WIDTH = len(grid[0])

    scores = generate_empty_grid(LENGTH, WIDTH)

    max_score = 0

    def calculate_sight(position, direction):
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        # 0 = down, 1 = right, 2 = up, 3 = left
        
        x, y = position
        current_height = grid[y][x]
        dx, dy = directions[direction]
        sight = 0
        while True:
            x += dx
            y += dy
            if x < 0 or x >= WIDTH or y < 0 or y >= LENGTH:
                break
            if grid[y][x] >= current_height:
                sight += 1
                break
            sight += 1
        return sight

    # iterate through the grid downwards
    for x in range(WIDTH):
        for y in range(LENGTH):
            down = calculate_sight((x, y), 0)
            right = calculate_sight((x, y), 1)
            up = calculate_sight((x, y), 2)
            left = calculate_sight((x, y), 3)
            score = down * right * up * left
            scores[y][x] = (down, right, up, left)
            max_score = max(max_score, score)
    print(scores)
    return max_score
            



if __name__ == '__main__':
    f = open('input.txt', 'r')
    
    inputarray = f.read().splitlines() 
    print(solution1(inputarray))
    print(solution2(inputarray))
