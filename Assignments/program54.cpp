// Name: Andre Sealy
// Email: andre.sealy72@myhunter.cuny.edu
// Date: April 23rd, 2024
// This program converts kilometers into miles

#include <iostream>
using namespace std;

int main() {
  double kilo, miles;
  cout << "Enter the number of kilometers: " << endl;
  cin >> kilo;
  miles = 0.621371 * kilo;

  cout << miles << endl;
}
