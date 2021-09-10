import timeit

setup1 = '''
import queue_to_do
print(queue_to_do.solution(0, 3))
print(queue_to_do.solution(17, 4))
print(queue_to_do.solution(100000, 1000))
'''


setup2 = '''
import queue_to_do2
print(queue_to_do2.solution(0, 3))
print(queue_to_do2.solution(17, 4))
print(queue_to_do2.solution(100000, 1000))
'''


setup3 = '''
import queue_to_do3
print(queue_to_do3.solution(0, 3))
print(queue_to_do3.solution(17, 4))
print(queue_to_do3.solution(100000, 1000))
'''
print(timeit.timeit(setup=setup1, number=1))
print(timeit.timeit(setup=setup2, number=1))
print(timeit.timeit(setup=setup3, number=1))
