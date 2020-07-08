import greatest_common_divisor as gcd


def test_odd_numbers():
    input_data = [15, 46, 32, 9, 10, 34, 21, 35]
    output_data = [15, 9, 21, 35]
    result = gcd.odd_numbers(input_data)
    assert output_data == result


def test_decompose_number():
    input_data = 720
    output_data = (2, 2, 2, 2, 3, 3, 5)
    result = gcd.prime_decompose(input_data)
    assert output_data == result


def test_gcd_prime_euclidean_algo():
    input_data = (480, 3312, 13212)
    output_data = 12
    result = gcd.greatest_common_divisor_euclidean_algo(input_data)
    assert output_data == result


def test_gcd_prime_numbers():
    input_data = (480, 3312)
    output_data = 48
    result = gcd.greatest_common_divisor_primes(input_data)
    assert output_data == result


def test_gcd_prime_euclidean_algo_single():
    input_data = (480,)
    output_data = 480
    result = gcd.greatest_common_divisor_euclidean_algo(input_data)
    assert output_data == result


def test_gcd_prime_numbers_single():
    input_data = (3312,)
    output_data = 3312
    result = gcd.greatest_common_divisor_primes(input_data)
    assert output_data == result


def test_factorial():
    input_data = 5
    output_data = 120
    result = gcd.factorial(input_data)
    assert output_data == result
