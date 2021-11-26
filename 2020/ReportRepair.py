def read_input():
    input_file = open("report_repair_input.txt")
    lines = input_file.readlines()

    collected_numbers = []
    for line in lines:
        collected_numbers.append(int(line))
    return collected_numbers

def find_pair(collected_numbers, goal_value):
    start = 0
    end = len(collected_numbers)
    for x in range(start, end, 1):
        for y in range(x, end, 1): 
            if collected_numbers[x] + collected_numbers[y] == goal_value:
                return x, y
    return 0,0

def find_solution_part1(collected_numbers, goal_value):
    x,y = find_pair(collected_numbers, goal_value)
    return collected_numbers[x] * collected_numbers[y]
# part 1 solution
print("part 1: ",find_solution_part1(read_input(), 2020))

# part 2

def find_sum_of_first_and_second_dict(collected_numbers):
    sums = {}
    start = 0
    end = len(collected_numbers)
    for x in range(start, end, 1):
        for y in range(x, end, 1):
            sums[collected_numbers[x] + collected_numbers[y]] = collected_numbers[x] * collected_numbers[y]
    return sums

def find_three_set(collected_numbers, goal_value):
    first_second_dict = find_sum_of_first_and_second_dict(collected_numbers)
    set_of_first_and_second = [x for x in first_second_dict.keys() if x < goal_value]

    for goal_number in collected_numbers:
        for matching_number in set_of_first_and_second:
            if goal_number + matching_number == goal_value and goal_number != 0 :
                print("goal value is ", goal_number, "matching is ", matching_number, "value is ", first_second_dict[matching_number])
                return first_second_dict[matching_number] * goal_number

print("part 2: ", find_three_set(read_input(), 2020))

