#include <iostream>
#include<string>
#include <vector>
#include <bits/stdc++.h> 

using namespace std;

void BubbleSort(std::vector<int>& values)
{
    for(size_t i = 0; i + 1 < values.size(); ++i)
    {
        for(size_t j = 0; j + 1 < values.size() - i; ++j)
        {
            if(values[j + 1] < values[j])
            {
                std::swap(values[j + 1], values[j]);
            }
        }
    }
}

int partition(std::vector<int>& values, int l, int r)
{
    int a = (l + r) / 2;
    int v = values[a];
    int i = l;
    int j = r;
    while(i <= j)
    {
        while(values[i] <  v)
        {
            ++i;
        }
        while(values[j] > v)
        {
            --j;
        }
        if (i >= j){
            break;
        }
        std::swap(values[i], values[j]);
        ++i;
        --j;
    }
    return j;   
}

void QuickSort(std::vector<int>& values, int l, int r)
{
    if (l < r)
    {
        int p = partition(values, l, r);
        QuickSort(values, p + 1, r);
        QuickSort(values, l, p);
    }
}



int main()
{
    int size = 10;


    // std::vector<int> vec = {5, 0, 1, 6, 3, 100 , 3, 40, 41, 40, 3, 6};
    std::vector<int> vec = {9, 8, 5, 6, 7};

    // std::vector<int> vec(size, 0);
    // srand(time(0));
    // generate(vec.begin(), vec.end(), rand);

    std::cout << "Random: ";
    for(size_t i = 0; i < vec.size(); ++i)
    {
        std::cout << vec[i] << ' ';
    } 
    std::cout << '\n';

    // BubbleSort(vec);
    QuickSort(vec, 0, vec.size() - 1);
    std::cout << "Sorted: ";
    for(size_t i = 0; i < vec.size(); ++i)
    {
        std::cout << vec[i] << ' ';
    }    
}