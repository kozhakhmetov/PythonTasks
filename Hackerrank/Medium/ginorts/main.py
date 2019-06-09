def greater(a, b):
    val_a = 0
    val_b = 0
    if a.islower():
        val_a = 0
    elif a.isupper():
        val_a = 1
    elif int(a) % 2:
        val_a = 2
    else:
        val_a = 3
    if b.islower():
        val_b = 0
    elif b.isupper():
        val_b = 1
    elif int(b) % 2:
        val_b = 2
    else:
        val_b = 3

    if val_a == val_b:
        if a < b:
            return -1
        return 1
    if val_a < val_b:
        return -1
    return 1


if __name__ == '__main__':
    s = raw_input()
    print ''.join(sorted(s, cmp=greater))
