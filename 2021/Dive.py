def get_input():
    input_file = open("dive_input.txt")
    lines = input_file.readlines()
    input_file.close()
    return lines

def part1(lines):
    x_axis = 0
    y_axis = 0
    for line in lines:
        direction, interval_str = line.split(" ")
        interval = int(interval_str)
        if direction == "forward":
            x_axis += interval
        if direction == "up":
            y_axis -= interval
        if direction == "down":
            y_axis += interval
    return x_axis * y_axis

print(part1(get_input()))

def part2(lines):
    aim = 0
    x_axis = 0
    y_axis = 0
    for line in lines:
        direction, interval_str = line.split(" ")
        interval = int(interval_str)
        if direction == "forward":
            y_axis += aim*interval
            x_axis += interval
        if direction == "up":
            aim -= interval
        if direction == "down":
            aim += interval
    return x_axis * y_axis

print(part2(get_input()))
