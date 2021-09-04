def solution(x, y):
    workerID = 1
    for r in range(y):
        workerID += r
    for c in range(y + 1, y + x):
        workerID += c
    return str(workerID)
