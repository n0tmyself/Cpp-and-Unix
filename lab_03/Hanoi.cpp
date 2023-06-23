#include <iostream>
#include<string>
#include <list>

using namespace std;

void Tower(int n, char from_rod, char to_rod, char aux_rod, list<string> &steps) {
    if (n == 1) {
        steps.push_back("disk 1 from " + string(1, from_rod) + " to " + string(1, to_rod));
        return;
    }

    Tower(n - 1, from_rod, aux_rod, to_rod, steps);
    steps.push_back("disk " + to_string(n) + " from " + string(1, from_rod) + " to " + string(1, to_rod));
    Tower(n - 1, aux_rod, to_rod, from_rod, steps);

}

int main() {
    int n;
    cout << "Enter the number of disks: ";
    cin >> n;
    list<string> steps;
    Tower(n, 'A', 'B', 'C', steps);
    int k = 0;

    for (string step : steps) {
        cout << step << endl;
        ++k;
    }
    cout << "Number of steps: " << k << endl;
    steps.clear();
    return 0;
}