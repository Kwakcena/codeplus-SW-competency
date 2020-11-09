#include <iostream>

using namespace std;

int n;
bool field[15][15];

// 위, \, / 방향의 대각선에 대해 퀸이 있는지 저장하는 배열
bool check_col[15];
bool check_dig1[40];
bool check_dig2[40];

bool check(int row, int col) {
  if(check_col[col]) {
    return false;
  }
  if(check_dig1[row + col]) {
    return false;
  }
  if(check_dig2[row - col + n]) {
    return false;
  }
  return true;
}

int calc(int row) {
  if(row == n) {
    return 1;
  }

  int cnt = 0;
  for(int col = 0; col < n; col++) {
    if(check(row, col)) {
      // field[row][col]에 퀸을 놓았으면
      // 해당 col, 대각선 방향은 퀸을 놓을 수 없음.
      check_dig1[row + col] = true;
      check_dig2[row - col + n] = true;
      check_col[col] = true;
      field[row][col] = true;
      
      cnt += calc(row + 1);

      check_dig1[row + col] = false;
      check_dig2[row - col + n] = false;
      check_col[col] = false;
      field[row][col] = false;
    }
  }

  return cnt;
}

int main() {
  cin >> n;
  cout << calc(0) << endl;
}