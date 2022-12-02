with open('inputs/day1.txt') as f:
    datas = f.read().splitlines()

top_calories = [0, 0, 0]
current_max = 0
for data in datas:
    if data != '':
        current_max += int(data)
    else:
        if top_calories[0] < current_max:
            top_calories[2] = top_calories[1]
            top_calories[1] = top_calories[0]
            top_calories[0] = current_max

        elif top_calories[1] < current_max:
            top_calories[2] = top_calories[1]
            top_calories[1] = current_max

        elif top_calories[2] < current_max:
            top_calories[2] = current_max

        current_max = 0

print("Top three Elves are carrying a total of", top_calories[0] + top_calories[1] + top_calories[2], "Calories.")
print("The first one is carrying", top_calories[0], "Calories.")
