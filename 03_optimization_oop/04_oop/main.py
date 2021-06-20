import re

class MonitoringAgent:
    def __init__(self, server_ip: str, access_key: str, period_get_data_s: int, period_send_data_s: int):
        self.__server_ip = server_ip
        self.__access_key = access_key
        self.__period_get_data_s = period_get_data_s
        self.__period_send_data_s = period_send_data_s
        self.__events_processed = 0

    @property
    def events(self):
        return self.__events_processed

    @events.setter
    def events(self):
        self.__events_processed += 1
        print(f"события сервера {self.__server_ip} собраны. Следующий сбор через {self.__period_get_data_s} секунд")
        return self.__events_processed

    def send_data(self):
        print(f"события сервера {self.__server_ip} собраны отправлены на сервер сбора метрик. \
            Следующиая отправка через {self.__period_send_data_s}секунд")

    def print_status(self):
        return f"С сервера {self.__server_ip} собрано {self.__events_processed } событий"

    @events.deleter
    def drop_cache(self):
        print("кеш агента был очищен")
        self.__events_processed = 0
        return self.__events_processed

    @property
    def period_get_data_s(self):
        return self.__period_get_data_s

    @period_get_data_s.setter
    def period_get_data_s(self, new_value):

        self.__period_get_data_s = time_parser(new_value)
        return f"New value is {self.__period_get_data_s}"


def time_parser(value):

    try:
        parsed_values = re.findall(r"\d+[hms]", value)
    except ValueError:
        return ValueError("Can't parse input value for period_get_data_s")

    parsed_values_s = 0

    for value in parsed_values:
        if "h" in value:
            digit_value = get_number(value)
            if not is_negative(digit_value):
                parsed_values_s += 3600 * digit_value
        if "m" in value:
            digit_value = get_number(value)
            if not is_negative(digit_value):
                parsed_values_s += 60 * digit_value
        if "s" in value:
            digit_value = get_number(value)
            if not is_negative(digit_value):
                parsed_values_s += digit_value

    return parsed_values_s


def get_number(value):
    return int(re.findall(r"\d+", value)[0])


def is_negative(number):
    if number < 0:
        raise ValueError("Time can't be a negative number")
    return False


if __name__ == '__main__':
    agent = MonitoringAgent(server_ip="1.2.3.4", access_key="secret", period_get_data_s=30, period_send_data_s=30)
    agent.period_get_data_s = "134m91s"
    print(agent.period_get_data_s)
