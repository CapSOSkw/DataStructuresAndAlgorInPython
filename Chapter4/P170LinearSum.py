def linear_sum(S, n):
    '''Return the sum of the first n numbers of S'''
    if n == 0:
        return 0
    else:
        return linear_sum(S, n-1) + S[n-1]


if __name__ == '__main__':
    s = [1, 2, 3, 4, 5]
    print(linear_sum(s, len(s)))