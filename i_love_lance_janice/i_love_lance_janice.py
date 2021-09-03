def solution(x):
    key = ord('a') + ord('z')
    x = ''.join(map(lambda c: chr(key - ord(c)) if c.islower() else c, x))
    return x
