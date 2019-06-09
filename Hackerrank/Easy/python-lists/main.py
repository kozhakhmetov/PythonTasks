if __name__ == '__main__':
    N = int(raw_input())
    result = []
    for i in range(N):
        input_ = raw_input().split()
        if input_[0] == 'insert':
            result.insert(int(input_[1]), int(input_[2]))
        if input_[0] == 'print':
            print result
        if input_[0] == 'remove':
            result.remove(int(input_[1]))
        if input_[0] == 'append':
            result.append(int(input_[1]))
        if input_[0] == 'sort':
            result.sort()
        if input_[0] == 'pop':
            result.pop()
        if input_[0] == 'reverse':
            result.reverse()
