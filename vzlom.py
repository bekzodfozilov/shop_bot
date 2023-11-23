# 1
import random

# son1 = int(input('1 sonni kiriting: '))
# list = []
# for i in range(son1):
#     l = []
#     for j in range(son1):
#         l.append(random.randrange(1, 9))
#     list.append(l)
# c = 1
# for i in range(son1):
#     for j in range(son1):
#         print(list[i][j], end=' ')
#     print()
# print('--------- ')
# temp = son1 - 1
# for i in range(son1):
#     for j in range(son1):
#         if i == j or temp == i + j:
#             list[i][j] = 0
#         print(list[i][j], end=' ')
#     print()

# 2
# list = []
# size = int(input('son kiriting: '))
# for i in range(size):
#     son = int(input(f'{i+1} sonni kiriting: '))
#     list.append(son)
# print(list)

# 3
# s = 'AsIlBeK'
# new = str()
# for i in s:
#     if i == i.lower():
#         new += i.upper()
#     else:
#         new += i.lower()
# print(new)

# 4
# son1 = int(input('1 sonni kiriting: '))
# son2 = int(input('2 sonni kiriting: '))
# list = []
# for i in range(son1):
#     l = []
#     for j in range(son2):
#         son = int(input(f'{i+1} {j+1} sonini kiriting:  '))
#         l.append(son)
#     list.append(l)

# 5
# count = [0 for i in range(26)]
# s = input('soz kiriting: ').lower()
# for i in s:
#     if i == 'a':
#         print('b', end='')
#     else:
#         print(i, end='')

# son1 = int(input('sonni kiriting: '))
# list = []
# for i in range(son1):
#     l = []
#     for j in range(son1):
#         l.append(random.randrange(1, 100))
#     list.append(l)
# print(list)
# max = list[0][0]
# min = list[0][0]
# max_index = int()
# min_index = int()
# for i in range(son1):
#     for j in range(son1):
#         if list[i][j] > max:
#             max = list[i][j]
#             max_index = [i, j]
#         if list[i][j] < min:
#             min = list[i][j]
#             min_index = [i, j]
# print(max_index, min_index)
# list[max_index[0]][max_index[1]] = min
# list[min_index[0]][min_index[1]] = max
# print(list)


