# coding=utf-8

# Количество свободной оперативной памяти в облачном кластере в мегабайтах
free_ram_amount = 300

# Количество реплик приложения
app_replicas = 2

# Есть ли возможность использовать дополнительную оперативную память при исчерпании лимита
has_ram_overdraft = True

# Баланс лицевого счета в местной валюте
balance = 1000

is_ram_enough = free_ram_amount - (app_replicas * 150) >= 0
is_money_enough = balance > 8000

print(app_replicas > 1 and (is_ram_enough or (is_money_enough and has_ram_overdraft)))

