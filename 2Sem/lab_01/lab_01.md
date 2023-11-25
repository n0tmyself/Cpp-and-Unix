# ЛР №1: Алгоритмы сортировки

## Цель

Познакомить студента с основами анализа алгоритмов на примере операций
сортировки.

## Задача

### 1. Быстрая сортировка

```C++
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
    // int l = 0;
    // int r = values.size() - 1;
    if (l < r)
    {
        int p = partition(values, l, r);
        QuickSort(values, p + 1, r);
        QuickSort(values, l, p);
    }
}
```

Временная сложность алогритма = $O \big(n log_2(n)\big)$

Затраты дополнительной памяти = $O\big( n \big)$

### 2. Сортировка пузырьком

```C++
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
```

Временная сложность алгоритма = $O \big(\frac{n(n-1)}{2} \big) = O \big(n^2 \big)$

Затраты дополнительной памяти = $O(1)$
