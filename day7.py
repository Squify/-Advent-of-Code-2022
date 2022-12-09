with open('inputs/day7.txt') as f:
    datas = f.read().splitlines()

sum = 0
for data in datas:
    # print(data, 'dir' in data, '$' in data)
    if 'dir' not in data and '$' not in data:
        test = data.split(' ')
        sum += int(test[0])

print(sum)