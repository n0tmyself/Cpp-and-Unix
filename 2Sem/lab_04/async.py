import asyncio
import time

# Время обработки для каждого действия
T1 = 0.1
T2 = 1
T3 = 0.5

# Количество пользователей для каждого действия
U1 = 5
U2 = 10
U3 = 20


# Параллельное выполнение с использованием asyncio
async def async_action_1(x=1):
    print(x ** 2)
    await asyncio.sleep(T1)
    print("Действие 1 выполнено")


async def async_action_2(x=2):
    print(x ** 2)
    await asyncio.sleep(T2)
    print("Действие 2 выполнено")


async def async_action_3(x=3):
    print(x ** 2)
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
end_time = time.time() - start_time
print("Параллельное выполнение с использованием asyncio заняло %s секунд" % end_time)

# print(type(tasks))
