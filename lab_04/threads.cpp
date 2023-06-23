#include <iostream>
#include <cmath>
#include <time.h>
#include <thread>
#include <mutex>

using namespace std;

double func1(const double &x){
    double res;
    res = x*x - x*x + pow(x, 4) - pow(x,5) + x + x;
    return res;
}

double func2(const double &x){
    double res;
    res = x + x;
    return res;
}

double func3(const double &func1, const double &func2){
    double res;
    res = func1 + func2 - func1;
    return res;
}

int main(){
    double x = 2.15;
    int n = 10000;
    double result1[n];
    double result2[n];
    double result3;
    std::mutex m;
    clock_t start = clock();

    std::thread th1([&result1, &x, &n, &m](){
        for (int i = 0; i<n; i++){
            m.lock();
            result1[i] = func1(x);
            m.unlock();
        }
    });

    std::thread th2([&result2, &x, &n, &m](){
        for (int i = 0; i<n; i++){
            m.lock();
            result2[i] = func2(x);
            m.unlock();
        }
    });

    for (int i = 0; i<n; i++){
        result3 = result1[i] + result2[i] - result1[i];
    }

    th1.join();
    th2.join();
    clock_t end = clock();
    double seconds = (double)(end - start) / CLOCKS_PER_SEC;
    std::cout << "Time of " << n << " : " << seconds <<" with threads \n";
    return 0;
}