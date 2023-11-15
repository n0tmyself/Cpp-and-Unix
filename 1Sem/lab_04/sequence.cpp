#include <iostream>
#include <cmath>
#include <time.h>

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

double time(const double &x, const int &n){
    clock_t start = clock();
    for (int i = 0; i < n; i++){
        double f1 = func1(x);
        double f2 = func2(x);
        double f3 = func3(f1, f2);
    }
    clock_t end = clock();
    double sec = (double)(end - start) / CLOCKS_PER_SEC;
    return sec;
}

int main() {
    double x = 2.15;
    int n = 10000;
    double seconds = time(x, n);
    std::cout << "Time of " << n << " : " << seconds <<" sequence \n";
    return 0;
}

