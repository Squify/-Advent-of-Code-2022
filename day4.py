with open('inputs/day4.txt') as f:
    datas = f.read().splitlines()

fully_contains = 0
overlaps = 0


def check_if_overlaps(elf_1_A, elf_1_B, elf_2_A, elf_2_B):
    if elf_1_A <= elf_2_A <= elf_1_B:
        return True

    elif elf_1_A <= elf_2_B <= elf_1_B:
        return True

    elif elf_2_A <= elf_1_A <= elf_2_B:
        return True

    elif elf_2_A <= elf_1_B <= elf_2_B:
        return True

    elif elf_1_A == elf_2_A or elf_1_B == elf_2_B:
        return True


for data in datas:
    assignment = data.split(',')
    elf_1 = assignment[0].split('-')
    elf_2 = assignment[1].split('-')

    if int(elf_1[0]) < int(elf_2[0]):
        if int(elf_1[1]) >= int(elf_2[1]):
            fully_contains += 1

    elif int(elf_1[0]) > int(elf_2[0]):
        if int(elf_1[1]) <= int(elf_2[1]):
            fully_contains += 1

    elif int(elf_1[0]) == int(elf_2[0]) or int(elf_1[1]) == int(elf_2[1]):
        fully_contains += 1

    if check_if_overlaps(int(elf_1[0]), int(elf_1[1]), int(elf_2[0]), int(elf_2[1])): overlaps += 1

print(fully_contains, "assignment pairs fully contains the other")
print(overlaps, "assignment pairs are overlaps")
