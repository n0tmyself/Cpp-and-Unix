# ЛР №4: Параллельные алгоритмы

## Цель

Познакомить студента с инструментами, направленными на решение
задач, использующих технологии распараллеливания.

## Задача

Моделирование нагрузки пользователей, которые обращаются почти
одновременно на сервер (запросы выстраиваются в очередь).

## Дано:

* Действие 1: Регистрация на портале (время обработки T1, нагрузка
на процессор ~25%)

* Действие 2: Получение главной страницы (время обработки T2,
нагрузка на процессор ~15%)

* Действие 3: Просмотр перечня зарегистрированных пользователей
(время обработки T3, нагрузка на процессор ~1%)

---

* U1 – количество пользователей, которые отправляют запрос на
действие 1

* U2 – количество пользователей, которые отправляют запрос на
действие 2

* U3 – количество пользователей, которые отправляют запрос на
действие 3

## Требуется:

Составить программу, на которой смоделировать поведение обработки
запросов пользователей. Рассмотреть вариант последовательного решения
задачи (1) и параллельных вариантах (рассмотреть каждый), subprocess (2),
threads (3), asyncio (4)


### Вывод
В ходе выполнения лабораторной работы были реализованы варианты последовательной реализации и несколько
вариантов параллельной реализации (```asyncio```, ```threading```, ```multiprocessing```). А также проведены измерения времени 
выполнения всех задач в каждом из вариантов. 
Реализации с помощью ```threading``` и ```asyncio``` показали почти одинаковые результаты, которые равны времени выполнения самой "медленной" задачи. 
Реализация с помощью ```multoprocessing``` имела более плохой результат, чем ```threading``` и ```asyncio```, однако время выполнения всех задач 
все равно было на порядок быстрее, чем в последовательном варианте

### Время работы различных реализаций

$$t_{\text{sequential}} \approx 20.8 \text{ seconds}$$

$$t_{\text{threading}} \approx 1.02 \text{ seconds}$$

$$t_{\text{asyncio}} \approx 1.02 \text{ seconds}$$

$$t_{\text{multiprocessing}} \approx 1.27 \text{ seconds}$$









