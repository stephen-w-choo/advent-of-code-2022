def get_elevation_a(hill):
    # takes a hill and returns an array of all the points at the lowest elevation

    res = []
    for y, row in enumerate(hill):
        for x, elevation in enumerate(row):
            if elevation == 1:
                res.append((x, y))

    return res

def convert_to_grid(inputarray):
    # takes an array of strings and converts it to a grid
    res = []

    for y, line in enumerate(inputarray):
        row = []
        for x, char in enumerate(line):
            if char == 'S':
                row.append(ord('a') - 96)
                start = (x, y)
                continue
            if char == 'E':
                row.append(ord('z') - 96)
                end = (x, y)
                continue
            row.append(ord(char) - 96)
        res.append(row)

    return res, start, end

def solution(inputarray, problem_number):
    hill, start, end = convert_to_grid(inputarray)

    neighbours = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # for the first problem the initial frontier is just the start node
    if problem_number == "1":
        currentfrontier = [start]
    # for the second problem the initial frontier is all the nodes at the lowest elevation
    if problem_number == "2":
        currentfrontier = get_elevation_a(hill)

    nextfrontier = []
    step = 0
    visited = set(currentfrontier)

    # breadth first search with no backtracking
    # if a node has been visited, it means there is already a quicker way to get there and there is no point in going back
    # maintain set of visited nodes to prevent backtracking

    while currentfrontier:
        for currentnode in currentfrontier:
            for neighbour in neighbours:
                newnode = (currentnode[0] + neighbour[0], currentnode[1] + neighbour[1])
                if newnode in visited: # check if node has been visited
                    continue
                if 0 <= newnode[0] < len(hill[0]) and 0 <= newnode[1] < len(hill): # check if node is in bounds
                    if hill[newnode[1]][newnode[0]] in range(1, hill[currentnode[1]][currentnode[0]] + 2): # check if node is reachable
                        if newnode == end: # return if node is at the end
                            return step + 1
                        visited.add(newnode)
                        nextfrontier.append(newnode) # add reachable nodes to the next frontier
        currentfrontier = nextfrontier # set the next frontier as the current frontier
        nextfrontier = [] # reset the next frontier
        step += 1 # increment the step


if __name__ == '__main__':
    f = open('input.txt', 'r')

    inputarray = f.read().splitlines()

    print(solution(inputarray, "1"))
    print(solution(inputarray, "2"))
