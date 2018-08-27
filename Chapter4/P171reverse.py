def reverse(S, start, stop):
    if start < stop - 1:
        S[start], S[stop-1] = S[stop-1], S[start]
        reverse(S, start+1, stop-1)
    return S


if __name__ == '__main__':
    s = [1, 2, 3, 4, 5]
    print(reverse(s, 0, len(s)))