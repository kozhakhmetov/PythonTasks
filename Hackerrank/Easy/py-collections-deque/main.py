from collections import deque

if __name__ == '__main__':
    n = int(raw_input())
    my_deque = deque()
    for i in range(n):
        input_ = raw_input().split()
        if len(input_) > 1:
            getattr(my_deque, input_[0])(input_[1])
        else:
            getattr(my_deque, input_[0])()
    print ' '.join(my_deque)
