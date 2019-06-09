from itertools import product

if __name__ == '__main__':
    n, mod = map(int, raw_input().split())
    lists = [map(lambda x: int(x) ** 2, raw_input().split())[1:] for i in range(n)]
    print max(map(lambda x: sum(x) % mod, list(product(*lists))))
