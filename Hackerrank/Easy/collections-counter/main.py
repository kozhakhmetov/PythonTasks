from collections import Counter

if __name__ == '__main__':
    n = int(raw_input())
    shoes = map(int, raw_input().split())
    count_shoes = Counter()

    for shoe in shoes:
        count_shoes[shoe] += 1

    customer_number = int(raw_input())
    result = 0
    for i in range(customer_number):
        x, y = map(int, raw_input().split())
        if count_shoes[x] > 0:
            count_shoes[x] -= 1
            result += y
    print result
