// Mystery C++, #2
#include <iostream>
using namespace std;

int main() {
  int sum = 3;
  while (sum < 10) {
    cout << sum;
    sum = sum + sum;
  }
}
