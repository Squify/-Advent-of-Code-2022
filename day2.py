# A for Rock, B for Paper, and C for Scissors = opponent
# X for Rock, Y for Paper, and Z for Scissors = player

# 1 for Rock, 2 for Paper, and 3 for Scissors
# 0 if you lost, 3 if the round was a draw, and 6 if you won

with open('inputs/day2.txt') as f:
    datas = f.read().splitlines()


def is_rock(shape):
    if shape == 'A' or shape == 'X':
        return True
    else:
        return False


def is_paper(shape):
    if shape == 'B' or shape == 'Y':
        return True
    else:
        return False


def is_scissors(shape):
    if shape == 'C' or shape == 'Z':
        return True
    else:
        return False


def count_point():
    score = 0
    for data in datas:
        shapes = data.split(' ')
        if is_rock(shapes[0]):
            if is_rock(shapes[1]):
                score = score + 1 + 3
            if is_paper(shapes[1]):
                score = score + 2 + 6
            if is_scissors(shapes[1]):
                score = score + 3 + 0

        elif is_paper(shapes[0]):
            if is_rock(shapes[1]):
                score = score + 1 + 0
            if is_paper(shapes[1]):
                score = score + 2 + 3
            if is_scissors(shapes[1]):
                score = score + 3 + 6

        elif is_scissors(shapes[0]):
            if is_rock(shapes[1]):
                score = score + 1 + 6
            if is_paper(shapes[1]):
                score = score + 2 + 0
            if is_scissors(shapes[1]):
                score = score + 3 + 3
    return score


print("The result is", count_point(), "if we count the points")


def result():
    score = 0
    for data in datas:
        shapes = data.split(' ')
        if shapes[1] == 'X':  # Lose
            if is_rock(shapes[0]):
                score = score + 3 + 0
            if is_paper(shapes[0]):
                score = score + 1 + 0
            if is_scissors(shapes[0]):
                score = score + 2 + 0

        elif shapes[1] == 'Y':  # Draw
            if is_rock(shapes[0]):
                score = score + 1 + 3
            if is_paper(shapes[0]):
                score = score + 2 + 3
            if is_scissors(shapes[0]):
                score = score + 3 + 3

        elif shapes[1] == 'Z':  # Win
            if is_rock(shapes[0]):
                score = score + 2 + 6
            if is_paper(shapes[0]):
                score = score + 3 + 6
            if is_scissors(shapes[0]):
                score = score + 1 + 6
    return score


print("The result is", result(), "for the calculated outcome")
