from collections import defaultdict

if __name__ == '__main__':
    n, m = map(int, raw_input().split())
    position = defaultdict(list)
    for i in range(1, n + 1):
        word = raw_input()
        position[word].append(i)
    for i in range(m):
        word = raw_input()
        if word in position:
            print ' '.join(map(str, position[word]))
        else:
            print -1
