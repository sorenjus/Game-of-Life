# Move to driver
grid = []
rows = 0
cols = 0


def load_file(file):
    file = open(file, "r")
    # Repeat for each song in the text file
    for line in file:
        # Let's split the line into an array called "fields" using the ";" as a separator:
        fields = line.split(" ")
    file.close()
    counter = 0
    global rows
    global cols
    global grid
    rows = int(fields[0])
    cols = int(fields[1])
    o = 0
    j = 0
    grid = [['0' for i in range(cols)] for j in range(rows)]

    counter = 2
    for o in range(rows):
        for j in range(cols):
            grid[o][j] = fields[counter]
            counter += 1
    return grid


def save_file(file):
    global rows
    global cols
    global grid
    f = open(file, "w")
    f.write(str(rows) + " ")
    f.write(str(cols))
    for i in range(rows):
        for j in range(cols):
            f.write(" " + grid[i][j])
    f.close()
    return 0


def mutate():
    global rows
    global cols
    global grid
    temp = [['0' for i in range(cols)] for j in range(rows)]

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1':
                if get_neighbors(i, j) < 2:
                    temp[i][j] = '0'
                if get_neighbors(i, j) == 2 or get_neighbors(i, j) == 3:
                    temp[i][j] = '1'
                if get_neighbors(i, j) > 3:
                    temp[i][j] = '0'
            else:
                if get_neighbors(i, j) == 3:
                    temp[i][j] = '1'
    grid = temp
    return


def get_neighbors(i, j):
    global rows
    global cols
    global grid
    neighbors = 0

    if 0 < i < rows - 1:
        if 0 < j < cols - 1:
            if grid[i][j + 1] == '1':
                neighbors += 1
            if grid[i][j - 1] == '1':
                neighbors += 1
            if grid[i - 1][j] == '1':
                neighbors += 1
            if grid[i + 1][j] == '1':
                neighbors += 1
            if grid[i + 1][j + 1] == '1':
                neighbors += 1
            if grid[i + 1][j - 1] == '1':
                neighbors += 1
            if grid[i - 1][j + 1] == '1':
                neighbors += 1
            if grid[i - 1][j - 1] == '1':
                neighbors += 1
    # top left
    if i == 0 and j == 0:
        if grid[i][j + 1] == '1':
            neighbors += 1
        if grid[i + 1][j] == '1':
            neighbors += 1
    # top right
    if i == 0 and j == cols - 1:
        if grid[i][j - 1] == '1':
            neighbors += 1
        if grid[i + 1][j] == '1':
            neighbors += 1
    # bottom right
    if i == rows - 1 and j == cols - 1:
        if grid[i][j - 1] == '1':
            neighbors += 1
        if grid[i - 1][j] == '1':
            neighbors += 1
    # bottom left
    if i == rows - 1 and j == 0:
        if grid[i][j + 1] == '1':
            neighbors += 1
        if grid[i - 1][j] == '1':
            neighbors += 1
    # Top row
    if i == 0 and 0 < j < cols - 1:
        if grid[i + 1][j] == '1':
            neighbors += 1
        if grid[i][j - 1] == '1':
            neighbors += 1
        if grid[i][j + 1] == '1':
            neighbors += 1
        if grid[i + 1][j + 1] == '1':
            neighbors += 1
        if grid[i + 1][j - 1] == '1':
            neighbors += 1
    # bottom row
    if i == rows - 1 and (0 < j < cols - 1):
        if grid[i - 1][j] == '1':
            neighbors += 1
        if grid[i][j + 1] == '1':
            neighbors += 1
        if grid[i][j - 1] == '1':
            neighbors += 1
        if grid[i - 1][j + 1] == '1':
            neighbors += 1
        if grid[i - 1][j - 1] == '1':
            neighbors += 1
    # left column
    if rows - 2 > i > 0 and j == 0:
        if grid[i][j + 1] == '1':
            neighbors += 1
        if grid[i - 1][j] == '1':
            neighbors += 1
        if grid[i + 1][j] == '1':
            neighbors += 1
        if grid[i + 1][j + 1] == '1':
            neighbors += 1
        if grid[i - 1][j + 1] == '1':
            neighbors += 1
    # right column
    if rows - 1 > i > 0 and j == cols - 1:
        if grid[i][j - 1] == '1':
            neighbors += 1
        if grid[i - 1][j] == '1':
            neighbors += 1
        if grid[i + 1][j] == '1':
            neighbors += 1
        if grid[i - 1][j - 1] == '1':
            neighbors += 1
        if grid[i + 1][j - 1] == '1':
            neighbors += 1
    return neighbors


def to_string():
    global rows
    global cols
    global grid
    string = ''
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '0':
                string += ' . '
            else:
                string += ' X '
        string += "\n"
    return string

'''
grid = load_file("glider.gol")
print(to_string())
grid = mutate()
print(to_string())
save_file("demofile3.txt")
'''