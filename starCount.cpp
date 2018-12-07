// Counting Stars

#include <iostream>
using namespace std;

int main()
{
	int i;
	int num;
	cout << "Enter a number: ";
	cin >> num;
	for (i = 0; i<=num; i++)
	{
		cout  << "*" * num;
	}
	return 0;
}