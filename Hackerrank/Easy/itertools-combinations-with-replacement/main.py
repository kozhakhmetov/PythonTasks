from itertools import combinations, combinations_with_replacement

if __name__ == '__main__':
    string, k = raw_input().split()
    k = int(k)
    string = sorted(string)
    print '\n'.join([''.join(i) for i in (combinations_with_replacement(string, k))])
