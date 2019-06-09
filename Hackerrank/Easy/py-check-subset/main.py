
if __name__ == '__main__':
    n = int(raw_input())
    for i in range(n):
        size_first = int(raw_input())
        first_set = set(map(int, raw_input().split()))
        size_second = int(raw_input())
        second_set = set(map(int, raw_input().split()))
        print first_set.intersection(second_set) == first_set
