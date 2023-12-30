import threading
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


start_time = time.time()

threads = []
for _ in range(U1):
    t = threading.Thread(target=action_1)
    threads.append(t)
    t.start()

for _ in range(U2):
    t = threading.Thread(target=action_2)
    threads.append(t)
    t.start()

for _ in range(U3):
    t = threading.Thread(target=action_3)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Параллельное выполнение с использованием threads заняло %s секунд" % (time.time() - start_time))
