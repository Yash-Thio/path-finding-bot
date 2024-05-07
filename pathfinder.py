import serial
maze_size = 5
def send_string_over_bluetooth(message, com_port):
    try:
        # Open serial port
        ser = serial.Serial(com_port, 9600, timeout=1)
        print("Serial port opened successfully")

        # Send the message
        ser.write(message.encode())
        print("Message sent over Bluetooth:", message)

        # Close serial port
        ser.close()
        print("Serial port closed")
    except serial.SerialException as e:
        print("Error:", e)
def is_valid_cell(cell):
    row, col = cell
    return 0 <= row < maze_size and 0 <= col < maze_size
def get_neighbors(cell):
    row, col = cell
    neighbors = []
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        new_row, new_col = row + dr, col + dc
        if is_valid_cell((new_row, new_col)):
            neighbors.append((new_row, new_col))
    return neighbors
def heuristic(current, goal):
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])
def solve_maze(maze, start, end):
    visited = set()
    open_set = [(heuristic(start, end), start)]
    came_from = {}

    while open_set:
        _, current = min(open_set)
        open_set.remove((heuristic(current, end), current))

        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path

        visited.add(current)

        for neighbor in get_neighbors(current):
            if maze[neighbor[0]][neighbor[1]] == 1 or neighbor in visited:
                continue
            tentative_g_score = heuristic(start, current) + heuristic(current, neighbor)
            if (heuristic(neighbor, end), neighbor) not in open_set:
                open_set.append((heuristic(neighbor, end), neighbor))
            elif tentative_g_score >= heuristic(start, neighbor):
                continue

            came_from[neighbor] = current

    return None

def path_to_string(path):
    directions = []
    for i in range(1, len(path)):
        curr_row, curr_col = path[i - 1]
        next_row, next_col = path[i]
        if next_row > curr_row:
            directions.append('S')
        elif next_row < curr_row:
            directions.append('N')
        elif next_col > curr_col:
            directions.append('E')
        elif next_col < curr_col:
            directions.append('W')
    return ''.join(directions)


if __name__ == "__main__":
    maze = [[0, 1, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 0, 0, 1], [0, 0, 0, 1, 1], [0, 1, 0, 1, 1]]

    # Print the maze
    print("Maze:")
    for row in maze:
        print(" ".join(str(cell) for cell in row))

    # Get start and end points from user
    start_row = int(input("Enter start row (0-4): "))
    start_col = int(input("Enter start column (0-4): "))
    end_row = int(input("Enter end row (0-4): "))
    end_col = int(input("Enter end column (0-4): "))

    # Solve the maze using A* algorithm
    start = (start_row, start_col)
    end = (end_row, end_col)
    path = solve_maze(maze, start, end)
    if path:
        # Convert the path to string
        path_str = path_to_string(path)
        print("Path:", path_str)
        com_port = 'COM6'
        # Send the message over Bluetooth
        send_string_over_bluetooth(path_str, com_port)
    else:
        print("No path found to reach the end point.")

