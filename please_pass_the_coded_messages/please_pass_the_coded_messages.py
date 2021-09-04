import itertools


def solution(l):
    largestNum = 0
    for n in range(len(l) + 1):
        permutationsLengthN = list(itertools.permutations(l, n))
        for p in permutationsLengthN:
            if p:
                num = int(''.join(map(str, p)))
                if num % 3 == 0 and num > largestNum:
                    largestNum = num
    return largestNum
