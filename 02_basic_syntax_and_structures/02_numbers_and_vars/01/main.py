# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
CONTAINERS_IN_POD = 4
PODS_IN_NODE = 117
NODES_IN_DC = 21


def count_dcs(containers_num):
    return containers_num / CONTAINERS_IN_POD / PODS_IN_NODE / NODES_IN_DC


def calc_free_memory(num_dcs):
    memory_limit_gb = 16
    memory_limit_mb = memory_limit_gb * 1024
    container_memory = 30
    return (memory_limit_mb * num_dcs * NODES_IN_DC) - containers * container_memory


def convert(result):

    return result // 1024, result % 1024


if __name__ == '__main__':
    containers = 68796
    number_dcs = count_dcs(containers)
    memory_free = calc_free_memory(number_dcs)
    human_result_gb, human_result_mb = convert(memory_free)
    print(int(number_dcs), int(memory_free), int(human_result_gb), int(human_result_mb))

