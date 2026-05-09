def square_pattern(n: int):
    for _ in range(n):
        print("*" * n)


square_pattern(5)


def stair_pattern(n: int):
    for i in range(1, n + 1):
        print("*" * i)


stair_pattern(5)


def stair_pattern_number(n: int):
    num = 0
    for i in range(1, n + 1):
        num = num * 10 + i
        print(num)


stair_pattern_number(5)


# def stair_pattern_same_number(n: int):
#     for i in range(1, n + 1):
#         print(i * (10 ** (i - 1)) + i)


# stair_pattern_same_number(5)
