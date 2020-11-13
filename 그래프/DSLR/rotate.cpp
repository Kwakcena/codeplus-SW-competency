#include<iostream>
#include<string>
#include<cmath>
#include<algorithm>

using namespace std;

int length(int number) {
  int n = 0;
  do {
    number = int(number/10);
    n++;
  } while(number > 0);
  return n;
}

int left_rotate(int n, int number) {
  int pow_number = (int)pow(10, n - 1);
  return (number % pow_number) * 10 + (number / pow_number);
}

int right_rotate(int n, int number) {
  int pow_number = (int)pow(10, n - 1);
  return (number / 10) + (number % 10) * pow_number;
}

void left_string_rotate(string &s) {
  rotate(s.begin(), s.begin() + 1, s.end());
}

void right_string_rotate(string &s) {
  rotate(s.rbegin(), s.rbegin() + 1, s.rend());
}

int main() {
  int number;
  string s = "abcdefg";

  int n = 0;

  cin >> number;
  n = length(number);


  cout << number << "를 왼쪽 회전 합니다." << endl;
  for(int r = 1; r <= n; r++) {
    number = left_rotate(n, number);
    cout << "회전 " << r << "번" << ": " << number << endl;
  }
  cout << "\n";

  cout << number << "를 오른쪽 회전 합니다." << endl;
  for(int r = 1; r <= n; r++) {
    number = right_rotate(n, number);
    cout << "회전 " << r << "번" << ": " << number << endl;
  }
  cout << "\n";

  cout << s << "를 왼쪽 회전 합니다." << endl;
  for(int r = 1; r <= n; r++) {
    left_string_rotate(s);
    cout << "회전 " << r << "번" << ": " << s << endl;
  }
  cout << "\n";

  cout << s << "를 오른쪽 회전 합니다." << endl;
  for(int r = 1; r <= n; r++) {
    right_string_rotate(s);
    cout << "회전 " << r << "번" << ": " << s << endl;
  }
  cout << '\n';
  return 0;
}