import subprocess
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

# Параллельное выполнение с использованием subprocess
start_time = time.time()

subprocess.Popen(["python", "action_1.py"])
subprocess.run(["python", "action_2.py", str(U2)])
subprocess.run(["python", "action_3.py", str(U3)])

print("Параллельное выполнение с использованием subprocess заняло %s секунд" % (time.time() - start_time))
