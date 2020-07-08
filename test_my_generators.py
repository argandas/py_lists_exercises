import my_generators as generators


def test_prime_generator():
    input_data = 30
    output_data = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)
    for i, p in enumerate(generators.primes_generator(input_data)):
        assert output_data[i] == p
    my_gen = generators.primes_generator(input_data)
    for data in output_data:
        assert data == next(my_gen)
