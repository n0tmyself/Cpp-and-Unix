import asyncio
import time

# Время обработки для каждого действия
T1 = 0.1
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

# Параллельное выполнение с использованием asyncio
async def async_action_1():
    await asyncio.sleep(T1)
    print("Действие 1 выполнено")

async def async_action_2():
    await asyncio.sleep(T2)
    print("Действие 2 выполнено")

async def async_action_3():
    await asyncio.sleep(T3)
    print("Действие 3 выполнено")

async def main():
    tasks = []
    for _ in range(U1):
        tasks.append(asyncio.create_task(async_action_1()))

    for _ in range(U2):
        tasks.append(asyncio.create_task(async_action_2()))

    for _ in range(U3):
        tasks.append(asyncio.create_task(async_action_3()))

    await asyncio.gather(*tasks)

start_time = time.time()
asyncio.run(main())
print("Параллельное выполнение с использованием asyncio заняло %s секунд" % (time.time() - start_time))