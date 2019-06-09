def minion_game(string_):
    first_score = 0
    second_score = 0
    for i in range(len(string_)):
        ch = string_[i]
        score = len(string_) - i
        if ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U':
            first_score += score
        else:
            second_score += score
    if first_score > second_score:
        print 'Kevin', first_score
    elif second_score > first_score:
        print 'Stuart', second_score
    else:
        print 'Draw'


if __name__ == '__main__':
    s = raw_input()
    minion_game(s)
