if __name__ == '__main__':
    n = int(raw_input())
    first_set = set(map(int, raw_input(). split()))
    m = int(raw_input())
    second_set = set(map(int, raw_input().split()))
    print '\n'.join(map(str, sorted(list(second_set.difference(first_set)
                                         .union(first_set.difference(second_set))))))
