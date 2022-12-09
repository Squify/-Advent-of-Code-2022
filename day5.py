with open('inputs/day5.txt') as f:
    datas = f.read().splitlines()

cargo = []
procedure = []

for data in datas:
    if 'move' not in data and data != '':
        cargo.append(data)
    elif 'move' in data:
        procedure.append(data)

cargo = cargo[::-1]
print(cargo)

column = 0
cargo_rearranged = []
for line in cargo:
    count = 0
    cargo_rearranged.append([''])
    print('Cargo :', cargo_rearranged, 'with column number', column)
    for content in line:
        if count != 3:
            print("___", content, "___ from line \"", line, "\" (character", count, ")")
            cargo_rearranged[0][column] += content
            count += 1
        else:
            print("___", content, "___ from line \"", line, "\" (character", count, "skipped)")
            count = 0
    column += 1
    print()

print(cargo_rearranged)
