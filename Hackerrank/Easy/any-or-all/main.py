from itertools import combinations, combinations_with_replacement, permutations

if __name__ == '__main__':
    string, k = raw_input().split()
    k = int(k)
    string = sorted(string)
    print '\n'.join([''.join(i) for i in (permutations(string, k))])
