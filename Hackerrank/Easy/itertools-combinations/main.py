from itertools import combinations, combinations_with_replacement

if __name__ == '__main__':
    string, k = raw_input().split()
    k = int(k)
    string = sorted(string)
    for i in range(1, k + 1):
        print '\n'.join([''.join(i) for i in (combinations(string, i))])
