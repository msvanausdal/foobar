def xor(x, y):
    if x % 2 == 0:
        xorRotation = [y, 1, y + 1, 0]
    else:
        xorRotation = [x, x ^ y, x-1, (x - 1) ^ y]
    return xorRotation[(x - y) % 4]


def solution(start, length):
    checksum = 0
    for i in range(0, length):
        checksum ^= xor(start+(length*i), start+(length*i)+(length-i)-1)
    return checksum
