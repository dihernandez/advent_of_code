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
        print("selected_occurrances is ", selected_occurrances)
        if selected_occurrances >= min_occur and selected_occurrances <= max_occur:
            tally_valid_passwords += 1
        else:
            print("right side is ", right_side, "min occur is ", min_occur, "max_occur is ", max_occur, "selected_letter ", selected_letter, "selected_occurrances is ", selected_occurrances)
    return tally_valid_passwords
#print(part1(["1-3 a: abcde","1-3 b: cdefg","2-9 c: ccccccccc"]))
print(part1(read_input()))
