import time

# Время обработки для каждого действия
T1 = 2
T2 = 1
T3 = 0.5

# Нагрузка на процессор для каждого действия
CPU_LOAD_T1 = 25
CPU_LOAD_T2 = 15
CPU_LOAD_T3 = 1

# Количество пользователей для каждого действия
U1 = 5
U2 = 10
U3 = 20

def action_1():
    time.sleep(T1)
    print("Действие 1 выполнено")

def action_2():
    time.sleep(T2)
    print("Действие 2 выполнено")

def action_3():
    time.sleep(T3)
    print("Действие 3 выполнено")

# Последовательное выполнение
start_time = time.time()

for _ in range(U1):
    action_1()

for _ in range(U2):
    action_2()

for _ in range(U3):
    action_3()

print("Последовательное выполнение заняло %s секунд" % (time.time() - start_time))
