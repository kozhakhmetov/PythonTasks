from collections import Counter

if __name__ == '__main__':
    n = int(raw_input())
    counter = Counter()
    inputs = []
    for i in range(n):
        input_string = str(raw_input())
        counter[input_string] += 1
        inputs.append(input_string)

    print len(counter)
    for string_ in inputs:
        if counter[string_]:
            print counter[string_],
            counter[string_] = 0

