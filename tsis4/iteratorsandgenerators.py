# 1

# def f(n):
#     for x in range(1, n + 1):
#         if x * x > n:
#             break
#         yield x * x
#
#
# print(*list(f(int(input()))))

# 2
# def f(n):
#     for x in range(0, n + 1, 2):
#         yield x
#
#
# print(*list(f(int(input()))))

# 3
# def f(n):
#     for x in range(0, n + 1):
#         if x % 3 and x % 4:
#             continue
#         yield x
#
#
# print(*list(f(int(input()))))
# 4
# def squares(a, b):
#     for x in range(int(a ** 0.5), int(b ** 0.5) + 1):
#         if x * x < a or x * x > b:
#             continue
#         yield x * x
#
#
# print(*list(squares(int(input()), int(input()))))
# 5
def f(n):
    for x in range(n, -1, -1):
        yield x


print(*list(f(int(input()))))
