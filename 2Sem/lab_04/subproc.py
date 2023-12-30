import multiprocessing
import time

# Время обработки для каждого действия
T1 = 0.1
T2 = 1
T3 = 0.5

# Количество пользователей для каждого действия
U1 = 5
U2 = 10
U3 = 20


def action_1(T, x=1):
    print(x ** 2)
    time.sleep(T)
    print("Действие 1 выполнено\n")


def action_2(T, x=2):
    print(x ** 2)
    time.sleep(T)
    print("Действие 2 выполнено\n")


def action_3(T, x=3):
    print(x ** 2)
    time.sleep(T)
    print("Действие 3 выполнено\n")


if __name__ == "__main__":
    processes = []
    start_time = time.time()
    for _ in range(U1):
        process = multiprocessing.Process(target=action_1, args=(T1,))
        processes.append(process)
        process.start()

    for _ in range(U1):
        process = multiprocessing.Process(target=action_2, args=(T2,))
        processes.append(process)
        process.start()

    for _ in range(U1):
        process = multiprocessing.Process(target=action_3, args=(T3,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print("Параллельное выполнение с использованием subprocess заняло %s секунд" % (time.time() - start_time))
