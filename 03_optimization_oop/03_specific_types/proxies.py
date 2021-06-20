from collections import deque
import re


def main():
    proxies = input()
    proxies_list = parse_input(proxies)
    serve_request(proxies_list)


def parse_input(input_str):
    """
    Validate entered string, parse it to list
    :param input_str: variable with string contains unparsed list
    :return: deque
    """
    try:
        for symbol in "[],\"":
            if symbol not in input_str:
                raise ValueError
        return deque(input_str.replace("[", "").replace("]", "").replace("\"", "").split(", "))

    except (TypeError, ValueError):
        print("Not a list!")
        raise


def is_allowed(proxy):
    """
    Check if proxy is banned or not
    :param proxy: list of proxies
    :return: Boolean. False if value should be filtered, True if value can be used
    """
    find_digit = int(re.findall(r"proxyhost(\d)\.slurm.io", proxy)[0])
    if find_digit % 3 == 0 or find_digit % 8 == 0:
        return False
    return True


def generate_proxies_queue(proxies):
    """
    Generator for creating queue of proxies
    :param proxies: list of proxies
    :return:
    """
    while True:
        yield proxies[0]
        used = proxies.popleft()
        proxies.append(used)


def serve_request(proxies):
    """
    Function that serves requests
    :param proxies: list of proxies
    :return:
    """
    gen = generate_proxies_queue(proxies)
    not_banned_proxies = [proxy for proxy in proxies if is_allowed(proxy)]
    for request in range(0, 1000):
        proxy = next(gen)
        print(f"Обращение при помощи прокси {proxy}")
        if is_allowed(proxy):
            print(f"Было осуществлено обращение к ресурсу при помощи прокси {proxy}")

    print(f"Не забанено {len(not_banned_proxies)} прокси.")


if __name__ == '__main__':
    main()
