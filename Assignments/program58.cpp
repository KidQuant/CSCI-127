// Name: Andre Sealy
// Email: andre.sealy72@myhunter.cuny.edu
// Date: April 23rd, 2024
// This program estimates the population in the future

#include <iostream>
using namespace std;

int main() {
  int years;
  int y = 2017;
  double p = 325.7;
  double B = 12.4 / 1000;
  double D = 8.4 / 1000;

  cout << "Please enter the number of years: " << endl;
  cin >> years;
  cout << "Year " << y << " " << p << endl;

  for (int i = 1; i < years; i++) {
    y += 1;
    p = p + (B * p) - (D * p);
    cout << "Year " << y << " " << p << endl;
  }
  return 0;
}
