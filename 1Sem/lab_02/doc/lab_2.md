# ЛР \#2: [C++ & UNIX]: C++ BUILD / IF / LOOP, PYTHON #

## Цель ##

Познакомить студента с принципами компиляции исходного кода. Составить
программу с использованием циклов, условий и функций. Сравнить быстродействие
между C++ и Python. Ознакомление с типами данных.

## Отчет ##

1. [С++ EXPRESSION] Создать и скомпилировать программу на C++.

Результат сборки (компиляции) сохранять в папку build. Папку build сделать
игнорируемой для GIT. Программа должна получать на вход число – это
количество итераций для выполнения расчета. В рамках итерации выполнять
следующее вычисление: x^2 - x^2 + x*4 - x*5 + x + x. Вычисление выполнять в виде
отдельной от main функции, которая будет вызвана циклически из main.
Фиксировать время выполнения программы, затрачиваемое на расчет выражения
n раз (n задается в консоли перед вычислением). Предусмотреть дополнительный
цикл на повторную итерацию запуска программы вычислений. Если было введено
не число, то завершить выполнение программы.


```C++
#include <iostream> 
#include <cmath> 
#include <time.h> 
#include <stdlib.h>

using namespace std;

double func(const int &x, const int &n) {
    clock_t start = clock();
    for(int i = 0; i < n; ++i)
    {
        float res = pow(x, 2) - pow(x, 2) + x * 4 - x * 5 + x + x;
    }; 
    clock_t end = clock();
    double seconds = (double)(end - start) / CLOCKS_PER_SEC;
    std::cout << seconds << endl;
    printf("Time is %.5e seconds\n", seconds);
    return seconds;
}

int main()
{
    string answer = "y";
    while (answer == "y")
    {
        float x = rand() % 2+100;

        int n; 
        std::cout << "Enter the number of iterations:" << endl;
        std::cin >> n;

        if(!std::cin.good())
        {
            std::cout << "That's not integer!!!" << endl;
            return 0;
        }
        std::cout << "That's integer" << endl;
        double res =  func(x, n);
        std::cout << "Do you want to repeat?: (y/n)" << endl;
        std::cin >> answer;
    }
}
```


2.[PYTHON EXPRESSION] Создать и скомпилировать программу на Python 3.

Результат сборки (компиляции) сохранять в папку build. Папку build сделать
игнорируемой для GIT. Программа должна получать на вход число – это
количество итераций для выполнения расчета. В рамках итерации выполнять
следующее вычисление: x ^2- x ^2+ x * 4 - x * 5+ x + x . Вычисление выполнять в виде
отдельной от main функции, которая будет вызвана циклически из main.
Фиксировать время выполнения программы, затрачиваемое на расчет выражения
n раз (n задается в консоли перед вычислением). Предусмотреть дополнительный
цикл на повторную итерацию запуска программы вычислений. Если было введено
не число, то завершить выполнение программы.


```python
import numpy as np
import timeit

input_n = input("Введите число итераций: ")

x = np.random.random()
print(x)

def f(x):
    return x**2 - x**2 + x*4 - x*5 + x + x

def time_measuring(function):
    try:
        n = int(input_n)
        print("Это целое число")
        print()
    except ValueError:
        print("Это не целое число!")
        return None
    time = timeit.timeit(stmt = "f(x)", globals = globals(), number = n)    
    return (n, time)

while True:
    n, time_res = time_measuring(f)
    if time_res == None:
        break
    else:
        print("Время выполнения", n, "итераций равно", time_res)
        print()
        answer = input("Хотите заново выполнить вычисления? (да/нет): ")
        if answer == "нет":
            break
```









