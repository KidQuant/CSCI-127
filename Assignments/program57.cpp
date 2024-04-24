// Name: Andre Sealy
// Email: andre.sealy72@myhunter.cuny.edu
// Date: April 23rd, 2024
// This program wants a specific number entered

#include <iostream>
using namespace std;

int main() {
  int year;
  cout << "Enter year:" << endl;
  cin >> year;
  while (year >= 2018) {
    cout << "Year must be 2018 or earlier" << endl;
    cout << "Enter year:" << endl;
    cin >> year;
  }
  cout << "You entered: " << year << endl;
}
