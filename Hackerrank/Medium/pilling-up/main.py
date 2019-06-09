def can_pill_up(size, cubes):
    stack = []
    for i in range(size):
        if cubes[0] > cubes[-1]:
            stack.append(cubes[0])
            cubes.pop(0)
        else:
            stack.append(cubes[-1])
            cubes.pop()
    if stack == sorted(stack, reverse=True):
        return 'Yes'
    return 'No'


if __name__ == '__main__':
    test_cases = int(raw_input())
    for i in range(test_cases):
        n = int(raw_input())
        cubes = map(int, raw_input().split())
        print can_pill_up(n, cubes)
