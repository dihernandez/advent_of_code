def read_input():
    input_file = open("sonar_sweep_input.txt")
    lines = input_file.readlines()
    input_file.close()
    return lines

def part1(lines):
    num_increases = 1
    for line_index in range(len(lines) - 1):
        if lines[line_index + 1] >= lines[line_index]:
            print("increasing ", lines[line_index], lines[line_index + 1])
            num_increases += 1

    return num_increases 

print(part1(read_input()))
