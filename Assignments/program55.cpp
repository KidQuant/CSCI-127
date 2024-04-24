// Name: Andre Sealy
// Email: andre.sealy72@myhunter.cuny.edu
// Date: April 23rd, 2024
// This program draws a triangle

#include <iostream>
using namespace std;

int main() {
  int n;
  cout << "Enter a triangle height:" << endl;
  cin >> n;
  for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= i; j++) {
      cout << "*";
    }
    cout << "\n";
  }
  return 0;
}
