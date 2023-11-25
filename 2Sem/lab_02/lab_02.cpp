#include <iostream>
#include <string>
#include <vector>
#include <bits/stdc++.h> 
#include <cstring>
#include <random>

using namespace std;


int main()
{



    int n = 6;
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

    double h[1 << n][n]; // h[mask][u] путь проходящий через вершины, соответсвуюший маске, заканчивающийся в вершине u (u не входит в маску)

    for (int i = 0; i < (1 << n); i++)
    {
        for (int j = 0; j < n; j++)
        {
            h[i][j] = INT_MAX;
        }
    }

    h[0][0] = 0;

    double best = INT_MAX;

    for (int mask = 0; mask < (1 << n); mask++) // пробегаемся по маскам
    {
        for (int u = 0; u < n; u++) // пробегаемся по вершинам u
        {
            if (h[mask][u] != INT_MAX) // смотрим только туда, где еще не были
            {
                int new_mask = mask | (1 << u); // записываем u в новую маску

                for (int v = 0; v < n; v++) // пробегаемся по вершинам на следующий шаг
                {
                    double weight = matrix_of_cities[u][v]; // записываем вес ребра

                    if (((new_mask & (1 << v))) == 0) // смотрим только туда, где еще не были
                    {
                        if (h[mask][u] + weight < h[new_mask][v]) // проверяем путь на оптимальность
                        {
                            h[new_mask][v] = h[mask][u] + weight; // если оптимальнее, то сохраняем его
                        }
                    }
                    if ((v == 0) && (new_mask == (1 << n) - 1) && (h[mask][u] + weight < best)) // если прошли всех и результат улучшули, сохраняем
                    {
                        best = h[mask][u] + weight;
                    }
                }
            }
        }
    }



    cout << "best = " << best << endl;
}