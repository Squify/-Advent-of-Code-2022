with open('inputs/day6.txt') as f:
    signal = f.read()


def found_packet(datas, size):
    character = 0
    for data in datas:  # TODO : redo
        packet_found = 0
        buffer = datas[character:(character + size)]
        for char in buffer:
            if buffer.count(char) > 1:
                character += 1
                break
            else:
                packet_found += 1
        if packet_found == size:
            return character + size


print('Start-of-packet is', found_packet(signal, 4))
print('Start-of-message is', found_packet(signal, 14))
