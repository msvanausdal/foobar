def solution(start, length):
    lastID = start + length**2-1
    lastIDLength = lastID.bit_length()
    invertBit = 0
    for b in range(lastIDLength):
        invertBit += 2**b
    checksumBits = []
    for b in range(lastIDLength):
        bitSum = 0
        nextID = start
        for row in range(length):
            for column in range(length):
                if nextID <= (start + (row * length) + (length - 1) - row):
                    bitSum += int(isBitSet(nextID, b))
                nextID += 1
        checksumBits.append((bitSum + 1) % 2)
    checksum = 0
    for b in reversed(checksumBits):
        checksum = (checksum << 1) | b
    checksum = bitNot(checksum, lastIDLength)
    return checksum


def bitNot(x, n):
    return (1 << n) - 1 - x


def isBitSet(x, n):
    return x & 1 << n != 0
