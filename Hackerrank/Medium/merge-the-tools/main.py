def merge_the_tools(s, block):
    result = [s[i:i + block] for i in range(0, len(s), block)]
    for i in result:
        print remain_first_occurrence(i)


def remain_first_occurrence(s):
    answer = ''
    for i in s:
        if i not in answer:
            answer += i
    return answer


if __name__ == '__main__':
    string, k = raw_input(), int(raw_input())
    merge_the_tools(string, k)
