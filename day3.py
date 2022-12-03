with open('inputs/day3.txt') as f:
    datas = f.read().splitlines()

caps = -38
minus = -96

priority_sum = 0
print(ord('A'), ord('a')) # 65 97

for data in datas:
    first_compartment = data[0:int(len(data)/2)]
    second_compartment = data[int(len(data)/2):len(data)]

    for letter in first_compartment:
        if letter in second_compartment:
            if letter.isupper():
                print(letter, ord(letter) + caps)
                priority_sum += ord(letter) + caps
            else:
                print(letter, ord(letter) + minus)
                priority_sum += ord(letter) + minus
            break


print(priority_sum)