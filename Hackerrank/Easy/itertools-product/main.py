from itertools import product

if __name__ == '__main__':
    A = map(int, raw_input().split())
    B = map(int, raw_input().split())
    for i in list(product(A, B)):
        print i,
