if __name__ == '__main__':
    set_size = int(raw_input())
    my_set = set(map(int, raw_input().split()))
    n = int(raw_input())
    for i in range(n):
        input_ = raw_input().split()
        if input_[0] == 'pop':
            my_set.pop()
        if input_[0] == 'remove':
            my_set.remove(int(input_[1]))
        if input_[0] == 'discard':
            my_set.discard(int(input_[1]))
    print sum(my_set)
