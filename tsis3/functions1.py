import itertools
import math
import random


def grams_to_ounces(grams):
    return 28.3495231 * grams


def fahrenheit_to_centigrade(F):
    return (5 / 9) * (F - 32)


# returns number of (chickens, rabbits) or if the data wrong
def solve(numheads, numlegs):
    for c in range(0, numheads + 1):
        if c * 2 + (numheads - c) * 4 == numlegs:
            return (c, numheads - c)
    return "wrong data"


# print(solve(35, 94))

def prime(x):
    if x < 2:
        return False
    for y in range(2, int(x ** (1 / 2)) + 1):
        if x % y == 0:
            return False
    return True


def filter_prime(l):
    res = []
    for x in l:
        if prime(x):
            res.append(x)
    return res


# print(filter_prime([2, 4, 13]))

def all_permutations(s):
    nums = list(s)
    permutations = list(itertools.permutations(nums))
    for permutation in permutations:
        print(''.join(permutation))


# all_permutations('ABC')

def has_33(nums):
    last = -1
    for x in nums:
        if last == 3 and x == 3:
            return True
        last = x
    return False


# print(has_33([1, 3, 3]), has_33([1, 3, 1, 3]), has_33([3, 1, 3]))

def spy_game(nums):
    needed = [7, 0, 0]
    for x in nums:
        if needed[-1] == x:
            needed.pop()
        if len(needed) == 0:
            return True
    return False


# print(spy_game([1,2,4,0,0,7,5]))
# print(spy_game([1,0,2,4,0,5,7]))
# print(spy_game([1,7,2,0,4,5,0]))

def volume_sphere(r):
    return math.pi * (r ** 3) * 4 / 3


# print(volume_sphere(6))
def unique_elements(nums):
    res = []
    for x in nums:
        if nums.count(x) == 1:
            res.append(x)
    return res


# print(unique_elements([2, 1, 2]))
def is_palindrome(s):
    s = list(s)
    return s == list(reversed(s))


# print(is_palindrome("aba"))
# print(is_palindrome("abc"))

def histogram(nums):
    for x in nums:
        print('*' * x)


# histogram([4, 9, 7])
def guess_number():
    name = input("Hello! What is your name?\n")

    print(f'Well, {name}, I am thinking of a number between 1 and 20.')
    guessed_number = random.randint(1, 20)

    x = -1
    while guessed_number != x:
        print("Take a guess.")
        x = int(input())

        print("")
        if x < guessed_number:
            print("Your guess is too low.")
        if x > guessed_number:
            print("Your guess is too high.")

    print(f'Good job, {name}! You guessed my number in {guessed_number} guesses!')


# guess_number()
