from math import sqrt

def bad_fib(n):
    if n <= 1:
        return 1

    else:
        return bad_fib(n-2) + bad_fib(n-1)


def good_fib(n):
    if n <= 1:
        return (n, 1)

    else:
        (a, b) = good_fib(n-1)
        return (a+b, a)


def fib1(n):
    a, b = 1, 1

    for i in range(n):
        yield a
        a, b = a+b, a

def fib2(n):
    return 1 if n <= 1 else int(((1 + sqrt(5)) ** n - (1 - sqrt(5)) ** n) / (2 ** n * sqrt(5)))



if __name__ == '__main__':
    print(list(fib1(5)))
    print(good_fib(5))
    print(bad_fib(5))
    print(fib2(5))