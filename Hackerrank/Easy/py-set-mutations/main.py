if __name__ == '__main__':
    n = int(raw_input())
    first_set = set(map(int, raw_input().split()))
    m = int(raw_input())
    for i in range(m):
        operation = str(raw_input().split()[0])
        my_set = set(map(int, raw_input().split()))
        if operation == 'intersection_update':
            first_set.intersection_update(my_set)
        if operation == 'update':
            first_set.update(my_set)
        if operation == 'symmetric_difference_update':
            first_set.symmetric_difference_update(my_set)
        if operation == 'difference_update':
            first_set.difference_update(my_set)
    print sum(first_set)