def num_idle_drivers(x, y):
    xrobots = {}
    yrobots = {}
    idleRobots = 0
    for index, xcoordinate in enumerate(x):
        try:
            xrobots[xcoordinate].append(y[index])
        except KeyError:
            xrobots[xcoordinate] = [y[index]]
        try:
            yrobots[y[index]].append(xcoordinate)
        except KeyError:
            yrobots[y[index]] = [xcoordinate]
    for key in xrobots.keys():
        xrobots[key].sort()
    for key in yrobots.keys():
        yrobots[key].sort()
    for index, xcoordinate in enumerate(x):
        ycoordinate = y[index]
        if xrobots[xcoordinate][0] < ycoordinate and xrobots[xcoordinate][-1] > ycoordinate and yrobots[ycoordinate][0] < xcoordinate and yrobots[ycoordinate][-1] > xcoordinate:
            idleRobots += 1
    return idleRobots

def numIdleDrives(x, y):
    from collections import defaultdict

    # Maps to store rows and columns
    x_map = defaultdict(set)
    y_map = defaultdict(set)

    n = len(x)

    # Populate x_map and y_map
    for i in range(n):
        x_map[x[i]].add(y[i])
        y_map[y[i]].add(x[i])

    idle_count = 0

    # Check each robot
    for i in range(n):
        # Check if there's any other robot in the same row or column
        has_neighbor_in_row = len(x_map[x[i]]) > 1
        has_neighbor_in_col = len(y_map[y[i]]) > 1

        if has_neighbor_in_row or has_neighbor_in_col:
            idle_count += 1

    return idle_count


x = [1, 1, 1, 2, 2, 2, 2, 3, 3, 3]
y = [1, 2, 3, 1, 2, 3, 5, 1, 2, 3]

print(num_idle_drivers(x, y))
print(numIdleDrives(x, y))

