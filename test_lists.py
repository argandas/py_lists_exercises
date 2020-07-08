import pytest
import lists_exercises as le


def test_get_largest_for():
    input_data = [15, 25, 180, 1000, 45]
    output_data = 1000
    result = le.get_largest_for(input_data)
    assert output_data == result


def test_get_largest_sort():
    input_data = [15, 25, 45]
    output_data = 45
    result = le.get_largest_sort(input_data)
    assert output_data == result


def test_get_largest_max():
    input_data = [15, 25, 180, 45]
    output_data = 180
    result = le.get_largest_max(input_data)
    assert output_data == result


def test_same_first_and_last_char():
    input_data = ["abc", "xyz", "aba", "1221"]
    output_data = 2  # ['aba', '1221']
    result = le.same_first_and_last_char(input_data)
    assert output_data == result


def test_sort_by_last():
    input_data = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    output_data = [(2, 5), (4, 4), (2, 3), (1, 2), (2, 1)]
    result = le.sort_by_last(input_data)
    assert output_data == result


def test_sort_by_freq():
    input_data = [2, 3, 4, 3, 10, 3, 5, 6, 3, 2, 2]
    output_data = [(3, 4), (2, 3), (4, 1), (5, 1), (6, 1), (10, 1)]
    result = le.sort_by_freq(input_data)
    assert output_data == result


def test_remove_duplicates():
    input_data = ["a", "b", "c", "d", "b", "a"]
    output_data = ["a", "b", "c", "d"]
    result = le.remove_duplicates(input_data)
    assert output_data == result


def test_filter_by_len():
    input_data = ["Hello", "is", "not", "World!"]
    output_data = ["Hello", "World!"]
    result = le.filter_by_len(input_data, 3)
    assert output_data == result


def test_check_for_common_element_true():
    input_data_1 = ["a", "b", "c", "d"]
    input_data_2 = ["d", "e", "f", "g"]
    output_data = True
    result = le.check_for_common_element(input_data_1, input_data_2)
    assert output_data == result


def test_check_for_common_element_false():
    input_data_1 = ["a", "b", "c"]
    input_data_2 = ["e", "f", "g"]
    output_data = False
    result = le.check_for_common_element(input_data_1, input_data_2)
    assert output_data == result


@pytest.fixture
def exercise8_input():
    pytest.input_data = [2, 3, 6, 3, 5, 8, 3, 4, 10, 2, 4]


def test_list_max(exercise8_input):
    output_data = 10
    result = le.list_max(pytest.input_data)
    assert output_data == result


def test_list_median(exercise8_input):
    output_data = 4
    result = le.list_median(pytest.input_data)
    assert output_data == result
    pytest.input_data.append(3)
    output_data = 3.5
    result = le.list_median(pytest.input_data)
    assert output_data == result


def test_list_nonrecurrent(exercise8_input):
    output_data = 6
    result = le.list_nonrecurrent(pytest.input_data)
    assert output_data == result


def test_list_most_recurrent(exercise8_input):
    output_data = [3]
    result = le.list_most_recurrent(pytest.input_data)
    assert output_data == result
