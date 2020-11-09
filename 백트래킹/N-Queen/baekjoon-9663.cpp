#include <iostream>

using namespace std;

int n;
int answer;
bool field[15][15];
bool visited_col[15];

bool check(int row, int col) {
  for(int i=0; i<row; i++) {
    if(field[i][col]) {
      return false;
    }
  }

  int y = row - 1, x = col - 1;
  while(y >= 0 && x >= 0) {
    if(field[y][x]) {
      return false;
    }
    y--, x--;
  }

  y = row - 1, x = col + 1;
  while(y >= 0 && x < n) {
    if(field[y][x]) {
      return false;
    }
    y--, x++;
  }
  return true;
}

void calc(int row) {
  if(row == n) {
    answer++;
    return;
  }

  for(int col = 0; col < n; col++) {
    if(visited_col[col]) continue;
    field[row][col] = true;
    visited_col[col] = true;

    if(check(row, col)) {
      calc(row + 1);
    }

    field[row][col] = false;
    visited_col[col] = false;
  }
}

int main() {
  cin >> n;
  calc(0);
  cout << answer;
}