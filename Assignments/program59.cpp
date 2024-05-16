// Name: Andre Sealy
// Email: andre.sealy72@myhunter.cuny.edu
// Date: April 23rd, 2024
// This program is the 'Two Complements' algorithm

#include <iostream>
using namespace std;

int main() {
  int n, x;
  int b = 16;

  cout << "Enter a number: " << endl;
  cin >> n;
  if (n < 0) {
    cout << 1;
    x = 32 + n;
  } else {
    cout << 0;
    x = n;
  }
  while (b > 0.5) {
    if (x >= b) {
      x %= b;
      cout << 1;
    } else {
      cout << 0;
    }
    b /= 2;
  }
  cout << '\n';
}
