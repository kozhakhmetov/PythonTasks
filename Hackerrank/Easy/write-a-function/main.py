def is_leap(year):
    return bool((not year % 400) or (not year % 4 and year % 100))


year = int(raw_input())
print is_leap(year)
