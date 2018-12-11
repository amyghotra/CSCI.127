//program 58
#include <iostream>
using namespace std;

int main()
{
    int birthYear;
    cout << "Enter your birth year: ";
    cin >> birthYear;
    while (birthYear > 2018)
    {
        cout << "Entered a future year\n";
        cout << "Please enter year born: ";
        cin >> birthYear;
    }
    
    cout << "You entered: " << birthYear;
    return 0;
}
