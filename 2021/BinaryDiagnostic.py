import collections

def read_input():
    input_file = open("binary_diagnostic_input.txt")
    lines = input_file.readlines()
    input_file.close()
    return lines

def find_most_common(input_string):
    options = {'0':0,'1':0}
    for char_s in input_string:
        options[char_s] += 1
    return '0' if options['0'] > options['1'] else '1'

def find_least_common(input_string):
    if find_most_common(input_string) == '0':
        return '1'
    else:
        return '0'

def part1(lines):
    gamma_str = ""
    epsilon_str = ""
    positions = {}
    for line in lines:
        for i in range(len(line) - 1):
            if i not in positions.keys():
                positions[i] = line[i]
            else:
                positions[i] = positions[i] + line[i]
    for key in range(len(positions.keys())):
        gamma_str += find_most_common(positions[key])
        epsilon_str += find_least_common(positions[key])
    return int(gamma_str, 2) * int(epsilon_str, 2)

print(part1(read_input()))

