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

        // cout << x[i] << " " << y[i] << endl;
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

    // если хочется посмотреть на матрицу, можно раскомментить
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