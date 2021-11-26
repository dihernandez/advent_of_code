import re

def read_input():
    to_read = open("password_philosophy_input.txt")
    lines = to_read.readlines()
    to_read.close()
    return lines

# part 1
def part1(lines):
    tally_valid_passwords = 0
    for line in lines:
        left_side = line[:line.find(":")]
        right_side = line[line.find(":") + 1: -1]
        min_occur, max_occur, selected_letter = re.split(r'-| ', left_side)
        min_occur = int(min_occur)
        max_occur = int(max_occur)
        selected_occurrances = right_side.count(selected_letter)
        if selected_occurrances >= min_occur and selected_occurrances <= max_occur:
            tally_valid_passwords += 1
    return tally_valid_passwords
print("part 1:")
print(part1(["1-3 a: abcde","1-3 b: cdefg","2-9 c: ccccccccc"]))
print(part1(read_input()))


# part 2
class DeconstructedLine():
    def __init__(self, line):
        self.left_side = line[:line.find(":")]
        self.right_side = line[line.find(":") + 1:].strip()
        min_index, max_index, self.selected_letter = re.split(r'-| ', self.left_side)
        self.min_index = int(min_index)
        self.max_index = int(max_index)


def part2(lines):
    unpacked_lines = [DeconstructedLine(line) for line in lines]
    tally_valid_passwords = 0
    for u_line in unpacked_lines:
        len_side = len(u_line.right_side)
        first_occur = u_line.right_side[u_line.min_index - 1] == u_line.selected_letter
        second_occur = u_line.right_side[u_line.max_index - 1] == u_line.selected_letter
        if first_occur ^ second_occur: 
            tally_valid_passwords += 1
    return tally_valid_passwords
print("part 2:")
print(part2(["1-3 a: abcde","1-3 b: cdefg","2-9 c: ccccccccc"]))
print(part2(read_input()))
