# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
CONTAINERS_IN_POD = 4
PODS_IN_NODE = 117
NODES_IN_DC = 21
MEMORY_LIMIT_GB = 16
MEMORY_LIMIT_MB = MEMORY_LIMIT_GB * 1024
CONTAINER_MEMORY = 30


if __name__ == '__main__':
    containers = 68796
    number_dcs = containers / CONTAINERS_IN_POD / PODS_IN_NODE / NODES_IN_DC
    memory_free = (MEMORY_LIMIT_MB * number_dcs * NODES_IN_DC) - containers * CONTAINER_MEMORY
    human_result_gb, human_result_mb = memory_free // 1024, memory_free % 1024
    print(int(number_dcs), int(memory_free), int(human_result_gb), int(human_result_mb))

