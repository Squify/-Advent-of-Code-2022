# A for Rock, B for Paper, and C for Scissors = opponent
# X for Rock, Y for Paper, and Z for Scissors = player
shape_score = {
    'rock': 1,
    'paper': 2,
    'scissors': 3
}


round_score = {
    'win': 6,
    'draw': 3,
    'lose': 0
}


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
                score = score + shape_score.get('rock') + round_score.get('draw')
            if is_paper(shapes[1]):
                score = score + shape_score.get('paper') + round_score.get('win')
            if is_scissors(shapes[1]):
                score = score + shape_score.get('scissors') + round_score.get('lose')

        elif is_paper(shapes[0]):
            if is_rock(shapes[1]):
                score = score + shape_score.get('rock') + round_score.get('lose')
            if is_paper(shapes[1]):
                score = score + shape_score.get('paper') + round_score.get('draw')
            if is_scissors(shapes[1]):
                score = score + shape_score.get('scissors') + round_score.get('win')

        elif is_scissors(shapes[0]):
            if is_rock(shapes[1]):
                score = score + shape_score.get('rock') + round_score.get('win')
            if is_paper(shapes[1]):
                score = score + shape_score.get('paper') + round_score.get('lose')
            if is_scissors(shapes[1]):
                score = score + shape_score.get('scissors') + round_score.get('draw')
    return score


print("The result is", count_point(), "if we count the points")


def result():
    score = 0
    for data in datas:
        shapes = data.split(' ')
        if shapes[1] == 'X':  # Lose
            if is_rock(shapes[0]):
                score = score + shape_score.get('scissors') + round_score.get('lose')
            if is_paper(shapes[0]):
                score = score + shape_score.get('rock') + round_score.get('lose')
            if is_scissors(shapes[0]):
                score = score + shape_score.get('paper') + round_score.get('lose')

        elif shapes[1] == 'Y':  # Draw
            if is_rock(shapes[0]):
                score = score + shape_score.get('rock') + round_score.get('draw')
            if is_paper(shapes[0]):
                score = score + shape_score.get('paper') + round_score.get('draw')
            if is_scissors(shapes[0]):
                score = score + shape_score.get('scissors') + round_score.get('draw')

        elif shapes[1] == 'Z':  # Win
            if is_rock(shapes[0]):
                score = score + shape_score.get('paper') + round_score.get('win')
            if is_paper(shapes[0]):
                score = score + shape_score.get('scissors') + round_score.get('win')
            if is_scissors(shapes[0]):
                score = score + shape_score.get('rock') + round_score.get('win')
    return score


print("The result is", result(), "for the calculated outcome")
