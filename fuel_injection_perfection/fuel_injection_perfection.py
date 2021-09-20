def solution(n):
    n = int(n)
    r = 0
    while n > 1:
        n = int(n)
        if n & 1 == 0:
            n >>= 2
        else:
            if n % 4 == 1 or n == 3:
                n -= 1
            else:
                n += 1
        r += 1
    return r
