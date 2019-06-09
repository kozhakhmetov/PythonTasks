from collections import Counter

if __name__ == '__main__':
    counter = Counter()
    k = int(raw_input())
    rooms = map(int, raw_input().split())
    for i in rooms:
        counter[i] += 1
    for i in counter:
        if counter[i] != k:
            print i
