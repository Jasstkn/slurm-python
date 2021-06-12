def main():
    rps_values = [5081, '17184', 10968, 9666, '9102', 12321, '10617', 11633, 5035, 9554, '10424', 9378, '8577', '11602',
                  14116, '8066', '11977', '8572', 9685, 11062, '10561', '17820', 16637, 5890, 17180, '17511', '13203',
                  13303, '7330', 7186, '10213', '8063', '12283', 15564, 17664, '8996', '12179', '13657', 15817, '16187',
                  '6381', 8409, '5177', 17357, '10814', 6679, 12241, '6556', 12913, 16454, '17589', 5292, '13639',
                  '7335',
                  '11531', '14346', 7493, 15850, '12791', 11288]

    while True:
        user_input = input()
        is_user_input_list = ("[" in user_input and "," in user_input and "]" in user_input)
        if user_input == "" or is_user_input_list:
            break
        elif ";" in user_input:
            rps_values.extend(user_input.split(";"))
        else:
            rps_values.append(int(user_input))

    int_rps_values = format_input(user_input, is_user_input_list, rps_values)
    average_load, median, numbers_frequency = get_params(int_rps_values)
    load_result = get_load_type(average_load, median)
    print(average_load, median, load_result)
    print(numbers_frequency)


def format_input(user_input, user_input_list, rps_values):
    """
    Accept raw data and type of the input
    :param user_input: User input
    :param user_input_list: Boolean variable for checking if user input is a list
    :param rps_values: Raw data
    :return: List with int values of data
    """
    if user_input_list:
        left, right = user_input[1:-1].split(",")
        return [int(element) for element in rps_values[int(left):int(right)]]
    else:
        return [int(element) for element in rps_values]


def get_params(load):
    """
    Get required values
    :param load: load: list with integers values
    :return: avg_load, median, numbers_frequency
    """
    avg_load = int(sum(load) / len(load))
    median = int(calc_median(load))
    numbers_frequency = get_frequency(load)
    return avg_load, median, numbers_frequency


def calc_median(load):
    """
    This function calculates median value of the list with load values
    :param load: list with integers values
    :return: median
    """
    sorted_load = sorted(load)
    quotient, remainder = divmod(len(sorted_load), 2)
    return sorted_load[quotient] if remainder else sum(sorted_load[quotient - 1:quotient + 1]) / 2


def get_load_type(avg_load, mdn_load):
    """
    Get load type
    :param avg_load: average value of the list
    :param mdn_load: median value of the list
    :return: type of the load
    """
    if avg_load < mdn_load:
        return "Снижения"
    if 0.75 * avg_load < mdn_load or mdn_load < 1.25 * avg_load:
        return "Стабильная"
    else:
        return "Скачки"


def get_frequency(load):
    """
    Get frequency for elements in the array
    :param load: list with integers values
    :return: return dictionary with values and frequency for each value
    """
    frequency_dict = {}
    for element in load:
        if element in frequency_dict.keys():
            frequency_dict[element] += 1
        else:
            frequency_dict[element] = 0
    return frequency_dict


if __name__ == '__main__':
    main()
