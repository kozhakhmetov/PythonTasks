if __name__ == '__main__':
    n = int(raw_input())
    for i in range(n):
        try:
            x, y = map(int, raw_input().split())
            print x / y
        except Exception as e:
            print "Error Code:", e
