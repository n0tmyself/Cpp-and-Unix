import time


# Время обработки для каждого действия
T1 = 0.1
T2 = 1
T3 = 0.5


# Количество пользователей для каждого действия
U1 = 5
U2 = 10
U3 = 20


def action_1(x=1):
    print(x ** 2)
    time.sleep(T1)
    print("Действие 1 выполнено\n")


def action_2(x=2):
    print(x ** 2)
    time.sleep(T2)
    print("Действие 2 выполнено\n")


def action_3(x=3):
    print(x ** 2)
    time.sleep(T3)
    print("Действие 3 выполнено\n")

# Последовательное выполнение
start_time = time.time()

for _ in range(U1):
    action_1()

for _ in range(U2):
    action_2()

for _ in range(U3):
    action_3()

print("Последовательное выполнение заняло %s секунд" % (time.time() - start_time))
