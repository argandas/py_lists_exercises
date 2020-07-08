import pluralsight_exercises as pse


def test_group_by_owners():
    output_data = {"Randy": ["Input.txt", "Output.txt"], "Stan": ["Code.py"]}
    input_data = {
        "Input.txt": "Randy",
        "Code.py": "Stan",
        "Output.txt": "Randy",
    }
    result = pse.group_by_owners(input_data)
    assert output_data == result


def test_icecream():
    output_data = [
        ["vanilla", "chocolate sauce"],
        ["chocolate", "chocolate sauce"],
    ]
    input_data_1 = ["vanilla", "chocolate"]
    input_data_2 = ["chocolate sauce"]
    my_instance = pse.IceCreamMachine(input_data_1, input_data_2)
    result = my_instance.scoops()
    assert output_data == result


def test_icecream_no_toppings():
    output_data = []
    input_data_1 = ["vanilla", "chocolate"]
    input_data_2 = []
    my_instance = pse.IceCreamMachine(input_data_1, input_data_2)
    result = my_instance.scoops()
    assert output_data == result


def test_icecream_no_ingredients():
    output_data = []
    input_data_1 = []
    input_data_2 = ["chocolate sauce"]
    my_instance = pse.IceCreamMachine(input_data_1, input_data_2)
    result = my_instance.scoops()
    assert output_data == result
