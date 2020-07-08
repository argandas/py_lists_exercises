import fizzbuzz as fb


def test_fizz_buzz():
    input_data = [15, 46, 32, 9, 10, 34, 21, 35]
    output_data = ["fizzbuzz", 46, 32, "buzz", "fizz", 34, "buzz", "fizz"]
    result = fb.fizzbuzz(input_data)
    assert output_data == result
