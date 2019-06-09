def is_leap(year):
    return bool((not year % 400) or (not year % 4 and year % 100))


if __name__ == '__main__':
    year = int(raw_input())
    print is_leap(year)
