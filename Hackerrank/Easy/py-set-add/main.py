if __name__ == '__main__':
    n = int(raw_input())
    countries = set()
    for i in range(n):
        country = raw_input()
        countries.add(country)
    print len(countries)