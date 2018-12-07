//program 57
#include <iostream>
using namespace std;

int main()
{
    int month;
    cout << "Enter a number";
    cin >> month;
    if (month < 3 or month > 11)
    {
        cout << "Happy Winter";
    }
    else if (month >= 3 and month < 7)
    {
       cout << "Happy Spring";
    }
    else if (month >= 7 and month < 9 )
    {
        cout << "Happy Summer";
    }
    else
    {
        cout << "Happy Fall";
    }

    return 0;
}
