//program 59
#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
    int x;
    double b;
    cout << setprecision(2) << fixed;
    cout << "Number:";
    b = 325.70;
    for (int i = 2017; i<2017+x; i++)
    {
        cout << "year" << i << b << "/n";
        b = b + b*12.4/1000 - b*8.4/1000;
    }

    return 0;
}
