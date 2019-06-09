import re

if __name__ == '__main__':
    s = raw_input()
    print re.match('^[4-6]([0-9]{10})', s).string
