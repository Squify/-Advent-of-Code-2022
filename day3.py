with open('inputs/day3.txt') as f:
    datas = f.read().splitlines()

uppercase_ascii_to_priority = -38
lowercase_ascii_to_priority = -96

priority_sum = 0

line_1, line_2, line_3 = '', '', ''
badges_sum = 0
line_count = 1

for data in datas:
    first_compartment = data[0:int(len(data) / 2)]
    second_compartment = data[int(len(data) / 2):len(data)]

    for letter in first_compartment:
        if letter in second_compartment:
            if letter.isupper():
                priority_sum += ord(letter) + uppercase_ascii_to_priority
            else:
                priority_sum += ord(letter) + lowercase_ascii_to_priority
            break

    if line_count == 1:
        line_1 = data
        line_count += 1
    elif line_count == 2:
        line_2 = data
        line_count += 1
    elif line_count == 3:
        line_3 = data
        for letter in line_3:
            if letter in line_1 and letter in line_2:
                if letter.isupper():
                    badges_sum += ord(letter) + uppercase_ascii_to_priority
                else:
                    badges_sum += ord(letter) + lowercase_ascii_to_priority
                break
        line_count = 1

print("The sum of the priorities of the error item is", priority_sum)
print("The sum of the badges priorities is", badges_sum)
