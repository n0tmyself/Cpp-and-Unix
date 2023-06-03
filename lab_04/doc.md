# ЛР #4: [C++ & UNIX]: C++ PROCESSES / THREADS #

## Цель ##

Познакомить студента с принципами параллельных вычислений. Составить несколько
программ в простейшими вычислительными действиями, чтобы освоить принципы
параллельных вычислений (когда одни алгоритмы зависят / не зависят от других).

## Отчет ##

1. [С++ SEQUENCE] Последовательные вычисления

Требуется последовательно выполнить вычисления по формуле 1, вычисления по
формуле 2, после чего выполнить вычисления по формуле 3, которые выглядят
следующим образом: результат вычислений 1 + результат вычислений 2 –
результат вычислений 1
Выполнить последовательно на 10 000 итераций и 100 000 итераций
Формула 1: f(x) = x ^2- x ^2+ x *4- x *5+ x + x
Формула 2: f(x) = x + x
Вывести длительность выполнения всех 10 000 итераций и 100 000 итераций в сек.

```C++
#include <iostream>
#include <cmath>
#include <time.h>


double func1(const double &x) {
    double res;
    res = pow(x, 2) - pow(x, 2) + 4*x - 5*x + x + x;
    // std::cout << res << "\n";
    return res; 
}

double func2 (const double &x) {
    double res;
    res = x + x;
    // std::cout << res << "\n";
    return res;
}

double func3(const double &f1, const double &f2) {
    double res;
    res = f1 + f2 - f1;
    return res;
}



double time_seq (const double &x, const int &n) {
    clock_t start = clock();
    for (int i = 0; i < n; i++) {
        double f1 = func1(x);
        double f2 = func2(x);
        double f3 = func3(f1, f2);
    }
    clock_t end = clock();
    double seconds = (double)(end - start)/CLOCKS_PER_SEC;
    return seconds;
}

int main() {
    double x = 0.1415;
    int n = 100000;
    double time_1 = time_seq(x, n);

    std::cout << "Time of " << n << " loops: " << time_1 << " seconds" << "\n";

    return 0;
}
```

2. [C++ THREADS] Параллельные вычисления через потоки

Требуется параллельно (насколько возможно с помощью процессов) выполнить
вычисления по формуле 1, вычисления по формуле 2, после чего выполнить
вычисления по формуле 3, которые выглядят следующим образом: результат
вычислений 1 + результат вычислений 2 – результат вычислений 1
Выполнить последовательно на 10 000 итераций и 100 000 итераций
Формула 1: f(x) = x ^2- x ^2+ x *4- x *5+ x + x
Формула 2: f(x) = x + x
Вывести длительность выполнения всех 10 000 итераций и 100 000 итераций в сек.
в разбивке по шагам вычислений 1, 2 и 3

```C++
#include <iostream>
#include <cmath>
#include <time.h>
#include <thread>
#include <mutex>


using namespace std;

float f1(const float &x) {
    return pow(x, 2) - pow(x, 2) + 4*x - 5*x + x + x;
}

float f2(const float &x) {
    return x + x;
}

int main() {
    float x = 0.1415;
    int n = 100000;
    float res_1[n];
    float res_2[n];
    float res_3;
    std::mutex m;
    clock_t start = clock();
    
    std::thread th1([&res_1, &x, &n, &m]()
    {   
        for (int i = 0; i<n; i++){
            m.lock();
            res_1[i] = f1(x);
            m.unlock();
        }
    });
    

    std::thread th2([&res_2, &x, &n, &m]()
    {   
        for (int i = 0; i<n; i++){
            m.lock();
            res_2[i] = f2(x);
            m.unlock();
        }
    });

    for (int i = 0; i < n; i++){
        res_3 = res_1[i] + res_2[i] - res_1[i];
    }
    th1.join();
    th2.join();
    clock_t end = clock();
    double seconds = (double)(end - start)/CLOCKS_PER_SEC;
    std::cout << "Time of " << n << " loops: " << seconds << " seconds" << "\n";
    return 0;
}
```

3. [C++ PROCESS] Параллельные вычисления через процессы

Требуется параллельно (насколько возможно с помощью процессов) выполнить
вычисления по формуле 1, вычисления по формуле 2, после чего выполнить
вычисления по формуле 3, которые выглядят следующим образом: результат
вычислений 1 + результат вычислений 2 – результат вычислений 1
Выполнить последовательно на 10 000 итераций и 100 000 итераций
Формула 1: f(x) = x ^2- x ^2+ x *4- x *5+ x + x
Формула 2: f(x) = x + x
Вывести длительность выполнения всех 10 000 итераций и 100 000 итераций в сек.
в разбивке по шагам вычислений 1, 2 и 3

```C++
#include <iostream>
#include <ostream>
#include <unistd.h>
#include <sys/wait.h>
#include <cmath>
#include <time.h>

float formula_1(const float& x){
    return std::pow(x, 2) - std::pow(x, 2) + x * 4 - x * 5 + x + x;
}

float formula_2(const float& x){
    return x + x;
}

int main() {
    float x = 0.1415;
    int n = 100000;
    float buf[n];

    clock_t start = clock();

    int pipe1[2], pipe2[2];
    if (pipe(pipe1) == -1 || pipe(pipe2) == -1) {
        std::cerr << "Failed to create pipes." << std::endl;
        return 1;
    }
    pid_t pid1 = fork();
    if (pid1 == -1) {
        std::cerr << "Failed to fork first child process." << std::endl;
        return 1;
    } else if (pid1 == 0) {
        // First child process
        
        float calc_1[n];
        for (int i = 0; i < n; i++) {
            close(pipe1[0]); // Close read end of pipe 1
            close(pipe2[0]); // Close read end of pipe 2
            close(pipe2[1]); // Close write end of pipe 2
            calc_1[i] = formula_1(x);
            write(pipe1[1], calc_1, sizeof(calc_1)); // Write result to pipe 1
            close(pipe1[1]); // Close write end of pipe 1
        }
        return 0;
    }
    pid_t pid2 = fork();
    if (pid2 == -1) {
        std::cerr << "Failed to fork second child process." << std::endl;
        return 1;
    } else if (pid2 == 0) {
        // Second child process
        float calc_2[n];
        for (int i = 0; i < n; i++) {
            close(pipe2[0]); // Close read end of pipe 2
            close(pipe1[0]); // Close read end of pipe 1
            close(pipe2[1]); // Close write end of pipe 2
            calc_2[i] = formula_2(x);
            write(pipe2[1], calc_2, sizeof(calc_2)); // Write result to pipe 2
            close(pipe2[1]); // Close write end of pipe 2

        }
        return 0;
    }
    // Parent process
    close(pipe1[0]); // Close read end of pipe 1
    close(pipe1[1]); // Close write end of pipe 1
    close(pipe2[1]); // Close write end of pipe 2
    float  calc_3;
    float calc_2[n];
    read(pipe2[0], calc_2, sizeof(calc_2)); // Read result from pipe 2
    float calc_1[n];
    read(pipe1[0], calc_1, sizeof(calc_1)); // Read result from pipe 1
    for (int i = 0; i < n; i++) {
        calc_3 = calc_1[i] + calc_2[i] - calc_1[i];
    }
    // Wait for child processes to exit
    int status;
    waitpid(pid1, &status, 0);
    waitpid(pid2, &status, 0);

    clock_t end = clock();
    double seconds = (double)(end - start) / CLOCKS_PER_SEC;
    std::cout << "Time of " << n << " loops is " << seconds << " seconds" << "\n";

    return 0;
}
```

## Время выполнения расчетов ##

1. Последовательные вычисления

Time of 10000 loops: 0.00 sec

Time of 100000 loops: 0.004 sec

2. Параллельные вычисления с помощью потоков

Time of 10000 loops: 0.004 sec

Time of 100000 loops: 0.021 sec

3. Параллельные вычисления с помощью процессов

Time of 10000 loops is 0.00017 sec

Time of 100000 loops is 0.000737 sec
