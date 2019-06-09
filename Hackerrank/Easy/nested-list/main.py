def main(names, scores):
    my_list = []
    my_set = set()
    for id_ in range(len(names)):
        my_list.append([names[id_], scores[id_]])
        my_set.add(scores[id_])
    return sorted([student[0] for student in my_list if student[1] == sorted(my_set)[1]])


if __name__ == '__main__':
    n = int(raw_input())
    name = []
    score = []
    for i in range(n):
        name.append(raw_input())
        score.append(float(raw_input()))
    print '\n'.join(main(name, score))
