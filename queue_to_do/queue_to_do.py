def solution(start, length):
    checksum = 0
    for r in range(length):
        checksum ^= (start + (length * r)) ^ (start + (length * (r + 1)) - 1)
    return checksum


'''
def solution(start, length):
    checksum = 0
    nextNum = start
    for r in range(length):
        for c in range(length):
            if nextNum <= (start + (r * length) + (length - 1) - r):
                checksum ^= nextNum
            nextNum += 1
    return checksum
'''
