//program 60
#include <iostream>
using namespace std;

int main()
{
    int n;
    int x;
    int b;
    b = 16;
    cout << "Enter a number between -31 and 31: ";
    cin >> n;
    if (n < 0)
    {
        cout << "1";
        x = 32 + n;
    }
    else
    {
        cout << "0";
        x = n;
    }
    while(b > 0.5)
    {
        if(x >= b)
        {
            cout << "1";
        }
        else
        {
            cout << "0";
        }
        x = x % b;
        b = b/2;
    }
    return 0;
}
