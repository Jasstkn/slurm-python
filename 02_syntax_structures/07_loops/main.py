def calc_average_load(load):
    avg_load = 0
    for element in load:
        avg_load += element

    return avg_load / len(cleaned_rps_values)


def calc_median_load(load):
    mdn_load = 0
    load = sorted(load)
    quotient, remainder = divmod(len(load), 2)
    return load[quotient] if remainder else sum(load[quotient - 1:quotient + 1]) / 2


def define_load_type(avg_load, mdn_load):
    if avg_load == mdn_load:
        load_type = "Стабильная"
    elif avg_load < mdn_load:
        load_type = "Снижения"
    else:
        load_type = "Скачки"

    return load_type


if __name__ == '__main__':
    rps_values = (5081, '17184', 10968, 9666, '9102', 12321, '10617', 11633, 5035, 9554, '10424', 9378, '8577', '11602',
                  14116, '8066', '11977', '8572', 9685, 11062, '10561', '17820', 16637, 5890, 17180, '17511', '13203',
                  13303, '7330', 7186, '10213', '8063', '12283', 15564, 17664, '8996', '12179', '13657', 15817, '16187',
                  '6381', 8409, '5177', 17357, '10814', 6679, 12241, '6556', 12913, 16454, '17589', 5292, '13639',
                  '7335',
                  '11531', '14346', 7493, 15850, '12791', 11288)

    cleaned_rps_values = [int(element) for element in rps_values]
    average_load = calc_average_load(cleaned_rps_values)
    median_load = calc_median_load(cleaned_rps_values)
    load_result = define_load_type(average_load, median_load)
    print(average_load, median_load, load_result)
