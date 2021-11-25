def read_input():
    input_file = open("report_repair_input.txt")
    lines = input_file.readlines()

    collected_numbers = []
    for line in lines:
        collected_numbers.append(int(line))
    return collected_numbers

def find_pair(collected_numbers):
    start = 0
    end = len(collected_numbers)
    for x in range(start, end, 1):
        for y in range(x, end, 1): 
            if collected_numbers[x] + collected_numbers[y] == 2020:
                return collected_numbers[x] * collected_numbers[y]
print(find_pair(read_input()))
