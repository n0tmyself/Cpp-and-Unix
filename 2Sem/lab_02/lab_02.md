# Лабораторная работа №2

### Структуры данных и динамическое программирование    
---
## Цель 

&ensp; Познакомить студента с основами структур данных и методикам динамического
программирования.

## Задание

&ensp; Поиск оптимального (кратчайшего, быстрейшего или самого дешевого) пути,
проходящего через промежуточный пункты по одному разу и возвращающегося в
исходную точку. К примеру, нахождение наиболее выгодного маршрута, позволяющего
коммивояжеру посетить со своим товаром определенные города по одному разу и
вернуться обратно. Мерой выгодности маршрута может быть минимальная длина
пути.

&ensp; Задать перечень точек с координатами X и Y. Пример:

- Точка 1, X1, Y1

- Точка 2, X2, Y2

- Точка 3, X3, Y3

- Точка ...
  
&ensp; В качестве отправной и конечной точки брать первую введенную точку.

1. Спроектировать оптимальную структуру для решения задачи с точки зрения
затрат памяти. Реализовать на языке C++ или Python

2. Спроектировать оптимальный алгоритм решения задачи с использованием
технологий динамического программирования. Оценить выислительные и
емкостные затраты. Реализовать на языке C++ или Python

## Решение


   ```C++
#include <iostream>
#include <string>
#include <vector>
#include <bits/stdc++.h> 
#include <cstring>
#include <random>

using namespace std;

int main()
{

    int n = 5;
    // cin >> n;

    double x[n], y[n];

    random_device rd;
    uniform_real_distribution<> dist(0, 15);
    
    for (int i = 0; i < n; i++)
    {
        x[i] = dist(rd);
        y[i] = dist(rd);

        cout << x[i] << " " << y[i] << endl;
    }

    double matrix_of_cities[n][n];

    for (int i = 0; i < n; i++)
    {
        for (int j = i; j < n; j++)
        {
            matrix_of_cities[i][j] = sqrt((x[i] - x[j]) * (x[i] - x[j]) + (y[i] - y[j]) * (y[i] - y[j]));
            matrix_of_cities[j][i] = matrix_of_cities[i][j];
        }
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cout << fixed << setprecision(2) << matrix_of_cities[i][j] << " ";
        }
        cout << endl;
    }

    double h[1 << n][n];

    for (int i = 0; i < (1 << n); i++)
    {
        for (int j = 0; j < n; j++)
        {
            h[i][j] = INT_MAX;
        }
    }

    h[0][0] = 0;

    double best = INT_MAX;

    for (int mask = 0; mask < (1 << n); mask++)
    {
        for (int u = 0; u < n; u++)
        {
            if (h[mask][u] != INT_MAX)
            {
                int new_mask = mask | (1 << u);

                for (int v = 0; v < n; v++)
                {
                    double weight = matrix_of_cities[u][v];

                    if (((new_mask & (1 << v))) == 0)
                    {
                        if (h[mask][u] + weight < h[new_mask][v])
                        {
                            h[new_mask][v] = h[mask][u] + weight;
                        }
                    }
                    if ((v == 0) && (new_mask == (1 << n) - 1) && (h[mask][u] + weight < best))
                    {
                        best = h[mask][u] + weight;
                    }
                }
            }
        }
    }

    cout << "best = " << best << endl;
}

   ```
#### Оценка сложности

Память $O(n 2^n)$
Cложность $O(n^2 2^n)$

### Результат

``` console

5.26218 13.6061
13.6416 6.14294
14.3958 2.45026
11.2276 14.2754
6.18026 9.49275
13.6042 3.82427
best = 33.40

```
