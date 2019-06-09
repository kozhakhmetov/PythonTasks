if __name__ == '__main__':
    main_set = set(map(int, raw_input().split()))
    n = int(raw_input())
    is_super_set = True
    for i in range(n):
        first_set = set(map(int, raw_input().split()))
        is_super_set &= main_set.issuperset(first_set)
    print is_super_set
