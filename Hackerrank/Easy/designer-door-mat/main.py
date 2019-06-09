def welcome(height, width):
    center_edge_size = (width - 7) / 2
    top_bottom_size = height / 2 + 1
    top = [('.|.' * (i * 2 - 1)).center(m, '-') for i in range(1, top_bottom_size)]
    bottom = top[::-1]
    return '\n'.join(top + ['-' * center_edge_size + 'WELCOME' + '-' * center_edge_size] + bottom)


if __name__ == '__main__':
    n, m = map(int, raw_input().split())
    result = welcome(n, m)
    print result
