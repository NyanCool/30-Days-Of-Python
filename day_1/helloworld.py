# Day 1 - 30DaysOfPython Challenge

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 ** 4)
print(3 % 4)
print(3 // 4)

print('Your name')
print('Your family name')
print('Your country')
print('I am enjoying 30 days of python')

# Checking data types
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4 + 4j))
print(type(['Asabeneh', 'Python', 'Finland']))
print(type('Your name'))
print(type('Your family name'))
print(type('Your country'))



from typing import Tuple
def euclidean_distance(p1: Tuple[int, int], p2: Tuple[int, int]):
    x1, y1 = p1
    x2, y2 = p2
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5

print(euclidean_distance((2,3), (10, 8)))

