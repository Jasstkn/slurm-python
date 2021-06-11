def calc_median(load):
    sorted_load = sorted(load)
    quotient, remainder = divmod(len(sorted_load), 2)
    return sorted_load[quotient] if remainder else sum(sorted_load[quotient - 1:quotient + 1]) / 2


def get_load_type(avg_load, mdn_load):
    if avg_load < mdn_load:
        return "Снижения"
    if avg_load - 0.25 * avg_load < mdn_load or mdn_load < avg_load + 0.25 * avg_load:
        return "Стабильная"
    else:
        return "Скачки"


def get_frequency(load):
    frequency_dict = {}
    for element in load:
        if element in frequency_dict.keys():
            frequency_dict[element] += 1
        else:
            frequency_dict[element] = 0
    return frequency_dict


if __name__ == '__main__':
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

    int_rps_values = [int(element) for element in rps_values]

    if is_user_input_list:
        left, right = user_input[1:-1].split(",")
        average_load = int(sum(int_rps_values[int(left):int(right)]) / len(int_rps_values[int(left):int(right)]))
        median = int(calc_median(int_rps_values[int(left):int(right)]))
        numbers_frequency = get_frequency(int_rps_values[int(left):int(right)])
    else:
        average_load = int(sum(int_rps_values) / len(int_rps_values))
        median = int(calc_median(int_rps_values))
        numbers_frequency = get_frequency(int_rps_values)
    load_result = get_load_type(average_load, median)
    print(average_load, median, load_result)
    print(numbers_frequency)