#include <iostream>
#include <cmath>
#include <string>

int main(int argc, char* argv[]) {
    double x, y;
    x = std::stod(argv[1]);
    y = std::stod(argv[3]);

    std::string oper;
    oper = argv[2];
    std::cout << oper << "\n";

    if (oper == "plus") {
        std::cout << x << '+' << y << '=' << x + y << "\n";
        return 0;
    }

    else if (oper == "minus") {
        std::cout << x << '-' << y << '=' << x - y << "\n";
        return 0;
    }

    else if (oper == "power") {
        double result = 1;
        for (int i = 0; i < y; i++) {
            result *= x;
        }
        std::cout << x << '^' << y << '=' << result << "\n";
        return 0;
    }

    else {
        std::cout << "Wrong operator" << "\n";
        return 0;
    }
}