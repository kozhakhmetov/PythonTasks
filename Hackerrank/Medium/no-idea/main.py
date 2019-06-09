def get_score(array, first_set, second_set):
    score = 0
    for i in array:
        if i in first_set:
            score += 1
        if i in second_set:
            score -= 1
    return score


if __name__ == '__main__':
    n, m = map(int, raw_input().split())
    array = map(int, raw_input().split())
    first_set = set(map(int, raw_input().split()))
    second_set = set(map(int, raw_input().split()))
    print get_score(array, first_set, second_set)