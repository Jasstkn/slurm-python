def main():
    hosts = input()
    commands = input()
    hosts_list, commands_list = validate_parse_input(hosts), validate_parse_input(commands)
    execute_commands(hosts_list, commands_list)


def validate_parse_input(input_str):
    """
    Validate entered string, parse it to list
    :param input_str: variable with string contains unparsed list
    :return: list
    """
    try:
        for symbol in "['],":
            if symbol not in input_str:
                raise ValueError
        return input_str.replace("[", "").replace("]", "").replace("'", "").split(", ")

    except (TypeError, ValueError):
        print("Not a list!")
        raise


def execute_commands(hosts, commands):
    for host in hosts:
        for command in commands:
            if command == "rm -rf /":
                print(f"На хосте {host} была попытка выполнить команду {command} , но процесс выполнения был аварийно остановлен.")
                break
            print(f"На хосте {host} была выполнена команда {command}")
        else:
            continue
        break


if __name__ == '__main__':
    main()
