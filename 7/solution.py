import re

def get_digits(inputstring):
    # takes a string and returns a list of integers
    digits = re.findall(r'\d+', inputstring)
    digits = map(int, digits)
    return list(digits)


def solution1(inputarray):
    adjacency_list = {}
    dir_size_dict = {}

    currentdir = ""
    # keep track of currentdirectory
    for line in inputarray:
        # if the line is a cd command
        if line[0:4] == "$ cd":
            # if the directory is "/"
            if line[5:] == "/":
                currentdir = ""
            # if the directory is ".."
            elif line[5:] == "..":
                # remove the last directory
                currentdir = currentdir[:currentdir.rfind('/')]
            else:
            # if the directory is a normal directory
                currentdir = currentdir + "/" + line[5:]
            continue
        # if the line is a ls command
        if line[0:4] == "$ ls":
            continue
        # if the line is listing a directory, add it to the adjacency list
        if line[0:3] == "dir":
            if currentdir == "":
                dirname = "root"
            else:
                dirname = currentdir
            if dirname not in adjacency_list:
                adjacency_list[dirname] = []
            adjacency_list[dirname].append(currentdir + "/" + line[4:])
            continue

        # otherwise parse any numbers as the size
        digits = get_digits(line)
        if digits:
            size = digits[0]
            if currentdir == "":
                dirname = "root"
            else:
                dirname = currentdir
            if dirname not in dir_size_dict:
                dir_size_dict[dirname] = 0
            dir_size_dict[dirname] += size
    
    print(adjacency_list)
    print(dir_size_dict)

    res = [0]

    def recursion(node):
        # base case
        if node not in dir_size_dict:
            dir_size_dict[node] = 0

        if node not in adjacency_list:
            if dir_size_dict[node] < 100000:
                res[0] += dir_size_dict[node]
            print(node, dir_size_dict[node])
            return dir_size_dict[node]
        # recursive case
        else:
            for child in adjacency_list[node]:
                dir_size_dict[node] += recursion(child)
            if dir_size_dict[node] < 100000:
                res[0] += dir_size_dict[node]
            print(node, dir_size_dict[node])
            return dir_size_dict[node]

    recursion("root")

    return res[0]

def solution2(inputarray):
    adjacency_list = {}
    dir_size_dict = {}

    currentdir = ""
    # keep track of currentdirectory
    for line in inputarray:
        # if the line is a cd command
        if line[0:4] == "$ cd":
            # if the directory is "/"
            if line[5:] == "/":
                currentdir = ""
            # if the directory is ".."
            elif line[5:] == "..":
                # remove the last directory
                currentdir = currentdir[:currentdir.rfind('/')]
            else:
            # if the directory is a normal directory
                currentdir = currentdir + "/" + line[5:]
            continue
        # if the line is a ls command
        if line[0:4] == "$ ls":
            continue
        # if the line is listing a directory, add it to the adjacency list
        if line[0:3] == "dir":
            if currentdir == "":
                dirname = "root"
            else:
                dirname = currentdir
            if dirname not in adjacency_list:
                adjacency_list[dirname] = []
            adjacency_list[dirname].append(currentdir + "/" + line[4:])
            continue

        # otherwise parse any numbers as the size
        digits = get_digits(line)
        if digits:
            size = digits[0]
            if currentdir == "":
                dirname = "root"
            else:
                dirname = currentdir
            if dirname not in dir_size_dict:
                dir_size_dict[dirname] = 0
            dir_size_dict[dirname] += size
    res = [0]

    def recursion(node):
        # base case
        if node not in dir_size_dict:
            dir_size_dict[node] = 0

        if node not in adjacency_list:
            return dir_size_dict[node]
        # recursive case
        else:
            for child in adjacency_list[node]:
                dir_size_dict[node] += recursion(child)
            return dir_size_dict[node]

    recursion("root")

    dir_sizes = list(dir_size_dict.values())

    dir_sizes.sort()

    return dir_sizes

if __name__ == '__main__':
    f = open('input.txt', 'r')
    
    inputarray = f.read().splitlines() 
    print(solution1(inputarray))
    print(solution2(inputarray))
