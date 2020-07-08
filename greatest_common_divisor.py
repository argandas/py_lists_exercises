import operator
import functools
import my_generators as gen


# Define if a number is odd
def is_odd(x):
    return bool(x % 2)


# Filter even numbers from a list
def odd_numbers(my_list):
    my_list = [x for x in my_list if is_odd(x)]
    return my_list


# Decompose a number into prime numbers
def prime_decompose(num):
    output = []
    for prime in gen.primes_generator(num):
        while num % prime == 0:
            output.append(prime)
            num /= prime
    return tuple(output)


# Get a tuple of common elements between 2 tuples
def get_common_elements(tuple1, tuple2):
    list1 = list(tuple1)
    list2 = list(tuple2)
    common = []
    for _, num1 in enumerate(list1):
        if num1 in list2:
            for index2, num2 in enumerate(list2):
                if num1 == num2:
                    list2.pop(index2)
                    common.append(num2)
                    break
    return tuple(common)


# Return the Maximum Common Divisor of 2 numbers
# This function uses the Euclidean Algorithm
def gcd_euclidean_algo(a=0, b=0):
    if a == 0:
        return b
    return gcd_euclidean_algo(b % a, a)


# Return the Maximum Common Divisor of a list of numbers
# This function uses the prime numbers method
def greatest_common_divisor_primes(nums):
    primes = tuple((prime_decompose(x)) for x in nums)
    reduced_common = functools.reduce(get_common_elements, primes)
    gcf = functools.reduce(operator.mul, reduced_common)
    return gcf


def greatest_common_divisor_euclidean_algo(nums):
    return functools.reduce(gcd_euclidean_algo, nums)


# Calculate a number factorial
def factorial(num: int):
    return functools.reduce(operator.mul, [num for num in range(1, num + 1)])
