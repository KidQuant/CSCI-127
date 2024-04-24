// Name: Andre Sealy
// Email: andre.sealy72@myhunter.cuny.edu
// Date: April 23rd, 2024
// This program greets you based on the month of the year

#include <iostream>
using namespace std;

int main() {
  int month;
  cout << "Enter month (as a number)" << endl;
  cin >> month;
  if ((month < 3) or (month > 11)) {
    cout << "Happy Winter" << endl;
  } else if ((month >= 3) and (month < 7)) {
    cout << "Happy Spring" << endl;
  } else if ((month >= 7) and (month < 9)) {
    cout << "Happy Summer" << endl;
  } else {
    cout << "Happy Fall" << endl;
  }
  return 0;
}
