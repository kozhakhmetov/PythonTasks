if __name__ == '__main__':
    n = int(raw_input())
    first_set = set(map(int, raw_input().split()))
    m = int(raw_input())
    second_set = set(map(int, raw_input().split()))
    print len(second_set.intersection(first_set))
