# Get largest number from a list using the sort() method
def get_largest_sort(my_list):
    my_list.sort(reverse=True)
    return my_list[0]


# Get largest number from a list using a for loop
def get_largest_for(my_list):
    max = my_list[0]
    for num in my_list:
        if num > max:
            max = num
    return max


# Get largest number from a list using the built-in max function
def get_largest_max(my_list):
    return max(my_list)


# 1) Return the count of list elements with the same first and last character
#    Example input: ['abc', 'xyz', 'aba', '1221']
#    Expected output: 2
def same_first_and_last_char(str_list):
    count = 0
    for word in str_list:
        if len(word) > 0:
            if word[0] == word[len(word) - 1]:
                count += 1
    return count


# Sort a list by the last element of each tuple
def sort_by_last(tuple_list):
    tuple_list.sort(key=lambda x: x[-1], reverse=True)
    return tuple_list


# Sort a list of numbers by frequency
def sort_by_freq(my_list):
    freq = [(e, my_list.count(e)) for e in set(my_list)]
    freq.sort(key=lambda x: x[1], reverse=True)
    return freq


# Remove list duplicates
def remove_duplicates(my_list):
    return list(dict.fromkeys(my_list))


# Return the Max element of a given list
def list_max(my_list):
    return max(my_list)


# Return the median value of a given list
def list_median(my_list):
    median = []
    my_list.sort()
    index = (len(my_list) // 2) - 1
    if (len(my_list) % 2) == 0:
        index = (len(my_list) // 2) - 1
        median.append(my_list[index])
        median.append(my_list[index + 1])
    else:
        index = len(my_list) // 2
        median.append(my_list[index])
    return sum(median) / len(median)


# Return the first non-recurring element in a list
def list_nonrecurrent(my_list):
    return min(my_list, key=my_list.count)


# Return the most recurring element in a list
def list_most_recurrent(my_list):
    most_recurrent = set([max(my_list, key=my_list.count)])
    max_count = my_list.count(list(most_recurrent)[0])
    for item in my_list:
        if my_list.count(item) == max_count:
            most_recurrent.add(item)
    return list(most_recurrent)


# Remove lists elements with lenght less than "n"
def filter_by_len(my_list, n):
    new_list = []
    for item in my_list:
        if len(item) > n:
            new_list.append(item)
    return new_list


# Check if 2 lists share at least 1 element
def check_for_common_element(my_list1, my_list2):
    found = False
    for item1 in my_list1:
        for item2 in my_list2:
            if item1 == item2:
                found = True
                break
        if found:
            break
    return found
