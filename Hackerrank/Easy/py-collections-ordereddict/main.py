from collections import OrderedDict

if __name__ == '__main__':
    n = int(raw_input())
    ordinary_dictionary = OrderedDict()
    for i in range(n):
        input_ = raw_input().rsplit(' ', 1)
        ordinary_dictionary[input_[0]] = ordinary_dictionary.get(input_[0], 0) + int(input_[1])
    for i in ordinary_dictionary:
        print i, ordinary_dictionary[i]
