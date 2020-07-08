def fizzbuzz(my_list):
    for i, num in enumerate(my_list):
        if num % 5 == 0 and num % 3 == 0:
            my_list[i] = "fizzbuzz"
        elif num % 5 == 0:
            my_list[i] = "fizz"
        elif num % 3 == 0:
            my_list[i] = "buzz"
    return my_list
