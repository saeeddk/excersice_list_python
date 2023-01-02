#  exercise 1 of Lists

# def sum(my_list: list) -> int:
#     result = 0
#     for item in my_list:
#         if isinstance(item, int):
#             result += item
#     return result
#
#
# a = sum([[6, 7], 'ss', 1, 2, 3, "saeed"])
# print(a)


## ######################################
#  exercise 2 of Lists


# def multiply(my_list: int) -> int:
#     result = 1
#     for item in my_list:
#         if isinstance(item, int):
#             result *= item
#     return result
#
#
# a = multiply([[6, 7], 'ss', 1, 2, 3, "saeed"])

# print(a)


## ######################################
# exercise 3 of Lists

# def my_max(my_list: list) -> int:
#     result = 0
#     for item in my_list:
#         if isinstance(item, int) and (result == 0 or result < item) :
#             result = item
#     return result
#
#
# a = my_max(['aa', [1, 2, 3], 3, 4, 5, 'ss'])
# print(a)

## ######################################
#  exercise 4 of Lists

# def my_min(my_list: int) -> int:
#     result = 0
#     for item in my_list:
#         if isinstance(item, int) and (result == 0 or item < result):
#             result = item
#     return result
#
#
# a = my_min(['aa', [1, 2, 3], 3, 4, 5, 0, -1, 'ss'])
# print(a)

## ######################################
#  exercise 5 of Lists

# def my_count(my_list: str) -> int:
#     result = 0
#     for item in my_list:
#         if len(item) > 2 and item[0] == item[-1]:
#             result += 1
#     return result
#
#
# a = my_count(['abc', 'xyz', 'aba', '1221'])
# print(a)

## ######################################
#  exercise 6 of Lists

# def sort_list(my_list: list) -> list:
#     on_sorted_list = []
#     for index, item in enumerate(my_list):
#         on_sorted_list.append((item[-1], index))
#     on_sorted_list.sort()
#
#     result = []
#     for item in on_sorted_list:
#         result.append((my_list[item[-1]]))
#
#     print(result)
#
#
# my_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
#
# sort_list(my_list)
# my_list.sort(key=sort_list)
# print(my_list)


#####
# def last(n):
#     return n[-1]
#
#
# def sort_list_last(tuples):
#     return sorted(tuples, key=last)
#
#
# print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))


## ######################################
#  exercise 7 of Lists

# def duplicated_list(my_list: list) -> list:
#     new_list = []
#     for item in my_list:
#         if item in new_list:
#             continue
#         elif item not in new_list:
#             new_list.append(item)
#     return new_list
####   or
# def dupli_list(n: list) -> list:
#     n = list(set(n))
#     return n
#
#
# my_list = [1, 2, 3, 2, 3, 4, 5, 1]
# a = dupli_list(my_list)
# print(a)

## ######################################
#  exercise 8 of Lists

# def check_list(my_list: list) -> bool:
#     new_list = []
#     for item in my_list:
#         new_list.append(item)
#         if new_list is None:
#             print('This list is empty')
#         else:
#             print(new_list)
#### or
# def check(n: list) -> str:
#     if len(n) == 0:
#         return 'This list is empty'
#     else:
#         return 'This list is not empty'
#
#
# my_list = []
# a = check(my_list)
#
# print(a)

## ######################################
#  exercise 9 of Lists

# def copy_list(my_list: list) -> list:
#     return my_list.copy()
#
#
# my_list = [1, 1, 1, ]
# a = copy_list(my_list)
# print(a)


## ######################################
#  exercise 10 of Lists

# def long_words(n, str):
#     word_len = []
#     txt = str.split()
#     for x in txt:
#         if len(x) > n:
#             word_len.append(x)
#     return word_len
# print(long_words(3, "The quick brown fox jumps over the lazy dog"))


## ######################################
#  exercise 11 of Lists


# def common_list(list1, list2) -> bool:
#     for item in list1:
#         for x in list2:
#             if x == item:
#                 return True
#     else:
#         return 'not common'

## or


# def common(n, m: list) -> bool:
#     new_list = []
#     for item in n:
#         for item1 in m:
#             if item1 is item:
#                 new_list.append(item1)
#     if len(new_list) > 0:
#         return True
#     else:
#         return False
#
#
# list1 = [1, 8, 4, 7]
# list2 = [2, 5, 6]
# a = common(list1, list2)
# print(a)


## #########################
#  exercise 12 of Lists

# def personal_remove(n: list) -> list:
#     new_list = []
#     for index, item in enumerate(n):
#         if index == 0 or index == 4 or index == 5:
#             continue
#         else:
#             new_list.append(item)
#     return new_list
#
#
# my_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# a = personal_remove(my_list)
# print(a)


##  ###########################
#  exercise 13 of Lists

# array = [[['*' for col in range(6)] for col in range(4)]for row in range(3)]
# print(array)
#
# x = [1 for col in range(5)]
# print(x)
#
# for col in range(5):
#     print(1)

##  ###########################
#  exercise 14 of List

# def even_remove(n: list) -> list:
#     odd_list = []
#     for item in n:
#         if item % 2 == 0:
#             continue
#         else:
#             odd_list.append(item)
#     return odd_list
#
#
# list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 98, 34, 53, 21, 22, 37, 36]
#
# a = even_remove(list_num)
# print(a)

##  ###########################
#  exercise 15 of List

# def shuffle_list(n: list) -> list:
#     sample_set = set(n)
#     sample_list = list(sample_set)
#     return sample_list
#
#
# my_list = ['saeed', 2, 'salam', 10, (1:2)]
# a = shuffle_list(my_list)
#
# print(a)
# to set chera nemitonim  yek list ya bool dashte bashim --- khata hashable mideh


##  ###########################
#  exercise 16 of List

# def square_num(n, m: int) -> list:
#     new_list = []
#     for item in range(n, m):
#         new_list.append(item ** 2)
#     l1 = new_list[0:5]
#     l2 = new_list[-5:]
#
#     print(l1)
#     print(l2)
#
#
# a = square_num(1, 20)
#
#
# print(a)
# chera akharesh None chap mikone

##  ###########################
#  exercise 17 of List

# def square_num1(n, m: int) -> list:
#     new_list = []
#     for item in range(n, m):
#         new_list.append(item ** 2)
#
#     return new_list[6:]
#
#
# b = square_num1(1, 20)
# print(b)


##  ###########################
#  exercise 18 of List


# list_permutations = [1, 2, 3, '4', 4]
# num_len = len(list_permutations)


# def permutations(n: int) -> int:
#     if n == 1:
#         return 1
#     else:
#         return n * permutations(n - 1)
#
#
# a = permutations(num_len)
# print(a)

##  ###########################
#  exercise 19 of List

# l5 = [1, 2, 3, '4', 4]
# l6 = ['s',6, 7, 1, 2]
#
#
# def difference(list1, list2: list) -> list:
#     list_difference = []
#     for item in list1:
#         for item1 in list2:
#             if item1 == item:
#                 list_difference.append(item1)
#             else:
#                 continue
#     return list_difference
#
#
# a = difference(l5, l6)
# print(a)

##  ###########################
#  exercise 20 of List

# def access_index_list(n: list):
#     my_list = []
#     for index, item in enumerate(n):
#         my_list.append([index, item])
#     return my_list
#     # print(index, item)
#
#
# l6 = ['s', 6, 7, 1, 2]
#
# a = access_index_list(l6)
# print(a)

#
# def access_index_list1(n: list) -> object:
#     for item in n:
#
#         return f'element : {item}   index : {n.index(item)}'
#
#
# a = access_index_list1(l6)
# print(a)

#  chera akharesh None chap mikone???????


##  ###########################
#  exercise 21 of List

# list_character = ['apple', 'banana', 'saeed', '1']


# def character(n: list) -> str:
#     my_character = ''.join(n)
#     return my_character


# def character1(n: list) -> str:
#     my_character = ''
#     for item in list_character:
#         my_character += item
#     return my_character
#
#
# print(character1(list_character))

##  ###########################
#  exercise 22 of List


# def list_find_index(n: list):
#     my_list = []
#     for index, item in enumerate(n):
#         my_list.append([index, item])
#     x = input('pleas enter item of list : ')
#     return index
#
#
# l1 = [1, 6, 's', 4, [5, 6]]
# print(list_find_index(l1))


##  ###########################
#  exercise 23 of List

# def flat_list(n: list) -> list:
#     flatten_list = []
#     for item in n:
#         for x in item:
#             flatten_list.append(x)
#     return flatten_list
#
#
# l2 = [[1, 2, 3], [4, 5], '99', ['s', 6, 7]]
# a = flat_list(l2)
# print(a)
# ??????????????????????????????????????????
##  ###########################
#  exercise 24 of List

# l1 = [1, 2, 3, 4]
# l2 = ['s', [4, 5], 2]
#
#
# def list_add(n, m: list) -> list:
#     for item in n:
#         m.append(item)
#     return m
#
#
# a = list_add(l1, l2)
# print(a)


##  ###########################
#  exercise 25 of List

# l2 = [1, 3, 's', 2]
#
#
# def random_list(n: list):
#     m = set(n)
#     for item in m:
#         return item
#
#
# a = random_list(l2)
# print(a)


##  ###########################
#  exercise 26 of List


# l1 = [1, 1, 1, 0, 0]
# l2 = [1, 0, 0, 1, 1]
# l3 = [1, 1, 1, 0, 1]
#
#
#
#
# def circul(n, m: list) -> bool:
#     list_3 = n * 2
#     for x in range(0, len(n)):
#         z = 0
#         for y in range(x, x + len(n)):
#             if m[z] == list_3[y]:
#                 z += 1
#             else:
#                 break
#         if z == len(n):
#             return True
#     return False
#
#
# a = circul(l1, l2)
# print(a)

##  ###########################
#  exercise 27  28 of List


# def large_number(n: list) -> int:
#     num = 0
#     for item in n:
#         if item > num:
#             num = item
#     return num
#
#
# a = large_number(list_number)
# print(a)


# def maxmin(A):
#     maxi = A[0]
#     secondsmax = A[0]
#     mini = A[0]
#     secondmini = A[0]
#     for item in A:
#         if item > maxi:
#             maxi = item
#         elif secondsmax != maxi and secondsmax < item:
#             secondsmax = item
#         elif item < mini:
#             mini = item
#         elif secondmini != mini and secondmini > item:
#             secondmini = item
#     print("Largest element is ::>", maxi)
#     print("Second Largest element is ::>", secondsmax)
#     print("Smallest element is ::>", mini)
#     print("Second Smallest element is ::>", secondmini)
#
# list_number = [0, 12, 3, 14, 5]
# a = maxmin(list_number)
# print(a)


## bug dare  ##############


#
# def smallest_largest_number(n: list):
#     num_max = 0
#
#     num_min = n[0]

#     for item in n:
#         if item > num_max:
#
#             num_max = item
#         elif item < num_min:
#
#             num_min = item
#     return num_min, num_max
#
#
# a = smallest_largest_number(list_number)
# print(a)
#
my_list = [0, -26, 15, 1, 23, -64, 23, 76]


# def large_small_number(n: list):
#     new_list = []
#     while n:
#         min = n[0]
#         for x in n:
#             if x < min:
#                 min = x
#         new_list.append(min)
#         n.remove(min)
#     return f'The smallest is {new_list[0]} and the second smallest is  {new_list[1]} , and the second largest is {new_list[-2]} and the largest is {new_list[-1]}'
#
#
# print(large_small_number(my_list))


##  ###########################
#  exercise 29 of List

#
# def uniq(n: list):
#     n = list(set(n))
#     for item in n:
#         print(item)


# my_list = [1, 3, 4, 4, 5, 5, 's', 'b', 's']
#   a = uniq(my_list)
#  print()
# uniq(my_list)

# chera agar return bedim faghat avalin value ro print mikone


# def uniq(n : list):
#     new_list = []
#     for item in n :
#         if item not in new_list:
#             new_list.append(item)
#         else:
#             continue
#     return new_list
#
# my_list = [1, 3, 4, 4, 5, 5, 's', 'b', 's']
# a = uniq(my_list)
# print(a)


##  ###########################
#  exercise 30 of List
#
# my_list = [1, 3, 4, 4, 5, 5, 's', 'b', 's']


# def frequency(n: list):
#     my_dict = {}
#     for item in n:
#         if item in my_dict:
#             my_dict[item] += 1
#
#         else:
#             my_dict[item] = 1
#     return my_dict
#
#
# a = frequency(my_list)
# print(a)


##  ###########################
#  exercise 31 of List

# my_list = [1, 3, 4, 4, 5, 5, 's', 'b', 's']


# def counter(n: list, a, b: int):
#     my_num = 0
#     for item in range(a, b):
#         if a <= item <= b:
#             my_num += 1
#     return my_num
#
#
# a = counter(my_list, 1, 5)
# print(a)

# niaz be tozih


##  ###########################
#  exercise 32 of List
#
# my_list = [1, 3, [4, 4], 5, 5, 's', 'b', 's']


# def check_sublist(n: list) -> list:
#     sublist = []
#     for item in n:
#         if type(item) == list:
#             sublist.append(item)
#         else:
#             continue
#     return sublist
#
#
# a = check_sublist(my_list)
# print(a)


##  ###########################
#  exercise 33 of List

# my_list = [10, 30, 4]


# def generate_sublist(n: list):
#     B = []
#     for item in range(len(n) + 1):
#         for x in range(item + 1, len(n) + 1):
#             sub = my_list[item: x]
#             B.append(sub)
#     return B
#
#
# a = generate_sublist(my_list)
# print(a)


##  ###########################
#  exercise 34 of List


# def prime_number(n: int):
#     prime_list = []
#     for item in range(2, n + 1):
#         if item not in prime_list:
#             print(item)
#             for j in range(item * item, n + 1, item):
#                 prime_list.append(j)
#     return prime_list
#
#
# print(prime_number(18))


##  ###########################
#  exercise 35 of List


# sample_list = ['p', 'q']


# Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']

# def concatinat_list(n: list, m: int) -> list:
#     concat_list = []
#
#     for x in range(1, m + 1):
#         for item in n:
#             a = f'{item}{x}'
#             concat_list.append(a)
#     return concat_list
#
#
# print(concatinat_list(sample_list, 5))

##  ###########################
#  exercise 36 of List

# def identification(x):
#     ident_number = id(x)
#     return ident_number


# x = 3
# a = identification(x)
# print(a)

# chera har bar yek shomare id midahad


##  ###########################
#  exercise 37 of List

# l1 = [1, 2, 3, 4]
# l2 = [3, 5, 5, 4]


# def common_list(n, m: list):
#     co_list = []
#     for item in l1:
#         for x in l2:
#             if item == x:
#                 co_list.append(item)
#     return co_list
#
#
# a = common_list(l1, l2)
# print(a)


##  ###########################
#  exercise 38 of List

# sample_list = [100, 10, 20, 30, 40, 50]


# def change(n: list) -> list:
#     for item in range(0, len(n), 2):
#         sample_list[item], sample_list[item + 1] = sample_list[item + 1], sample_list[item]
#     return sample_list
#
#
# a = change(sample_list)
# print(a)

##  ###########################
#  exercise 39 of List

# sample_list = [11, 33, 50]


# def convert_list(n: list):
#     new = ''
#     for item in n:
#         item = str(item)
#         new += item
#     return new


# a = convert_list(sample_list)
#
# print(a)


##  ###########################
#  exercise 40 of List


# sample_list = ['About', 'Absolutely','only',  'After', 'Besides', 'Biblical', 'Bill', 'Billgone']

#
# def split_list(n: list):

# list_sort = []
# while n:
#     min = n[0]
#     for x in n:
#         if x < min:
#             min = x
#     list_sort.append(min)
#     n.remove(min)

# txt = ''
# for item in list_sort :
#     txt += f' {item}'
#
# new_txt = txt.split()
# return new_txt


# a = split_list(sample_list)
# print(a)


# ???????????????


##  ###########################
#  exercise 41 of List


# list_number = [4, 5, 3, 2, 6]

# def multiple_list(n: list):
#     new_list = []
#     for item in n:
#         item *= 2
#         new_list.append(item)
#     return new_list

#  ??????????????????
# def multiple_list():
#     num = 1
#     odd_list = []
#     even_list = []
#     while num <= 20:
#         if num % 2 != 0:
#             odd_list.append(num)
#             num += 1
#         elif num % 2 == 0:
#             even_list.append(num)
#             num += 1
#     return odd_list, even_list
#
#
# print(multiple_list())
# ??????????????????

# l1 = [1, 2, 3, 4, 5]
# l2 = [2, 3, 4]


# def multiple(n, m: list):
#     m_2 = []
#     m_3 = []
#     m_4 = []
#     for item in n:
#         for x in m:
#             if x == m[0]:
#                 m_2.append(x * item)
#             elif x == m[1]:
#                 m_3.append(x * item)
#             elif x == m[2]:
#                 m_4.append(x * item)
#             else:
#                 continue
#     return m_2, m_3, m_4
#
#
# print(multiple(l1, l2))

# ??????????????????

##  ###########################
#  exercise 42 of List

l1 = [10, 20, 30, 40, 50, 60]
l2 = [30, 40, 60, 70, 80]


def num(n, m: list):
    missing_value_l1 = []
    missing_value_l2 = []
    additional_l1 = missing_value_l2
    additional_l2 = missing_value_l1

    for x in n:
        for z in m:
            if x != z and x not in missing_value_l2:
                missing_value_l2.append(x)
            elif x != z and z not in missing_value_l1:
                missing_value_l1.append(z)

    for i in m:
        for j in missing_value_l2:
            if j == i:
                missing_value_l2.remove(j)

    for q in n:
        for w in missing_value_l1:
            if q == w:
                missing_value_l1.remove(w)

    return missing_value_l1, additional_l1, missing_value_l2, additional_l2


print(num(l1, l2))


##  ###########################
#  exercise 43 of List


# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
#
#
# def diff_list(n: list) -> list:
#     sub_list = []
#     max_spil = 2
#     for item in range(0, len(n), max_spil):
#         sub_list.append(n[item:item + max_spil])
#
#     for x in sub_list:
#         if x in sub_list[0:2]:
#             x = set(x)
#             print(x)
#         elif x in sub_list[2:4]:
#             x = str(x)
#             print(x)
#         else:
#             x = tuple(x)
#             print(x)
#
#
# diff_list(my_list)

# ????????????????????? line 933 nemishe dict bezari?  // Aya in ravesh dorosti baraye in soal hast?


##  ###########################
#  exercise 44 of List


# def generate_number_group(n: int):
#     list_number = []
#     group_number = []
#     i = 1
#     while i < n:
#         list_number.append(i)
#         i += 1
#
#     for item in range(0, len(list_number), 5):
#         group_number.append(list_number[item: item + 5])
#
#     return group_number
#
#
# print(generate_number_group(27))

my_listb = [[(5*x + y) for y in range(1,6)] for x in range(10)]
print(my_listb)
my_list = []
for x in range(10):
    a = []
    for y in range(1, 6):
        a.append((5 * x +y))
    my_list.append(a)
print(my_list)

##  ###########################
#  exercise 45 of List


# my_list = [(7, 0), (1, 2), (7, 8), (4, 3), (6, 9), (3, 4)]
#
# # solution 1
# new_list = []
# for x in my_list:
#     for y in x:
#         new_list.append(y)
# new_set = set(new_list)
# print(sorted(new_set))
