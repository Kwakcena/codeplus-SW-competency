#include <iostream>
#include <vector>
#include <utility>

using namespace std;

int a[10][10];
bool c[10][10];
bool c2[10][10];
bool c3[10][10];

vector<pair<int, int>> zero_pos;

int square(int row, int col) {
  return (row / 3) * 3 + (col / 3);
}

void go(int index) {
  if(index == (int)zero_pos.size()) {
    for(int i=0; i<9; i++) {
      for(int j=0; j<9; j++) {
        cout << a[i][j] << " ";
      }
      cout << endl;
    }
    cout << endl;
    exit(0);
  }

  int y = zero_pos[index].first;
  int x = zero_pos[index].second;
  for(int number=1; number <= 9; number++) {
    if(c[y][number] == 0 && c2[x][number] == 0 && c3[square(y, x)][number] == 0) {
      c[y][number] = c2[x][number] = c3[square(y, x)][number] = true;
      a[y][x] = number;
      go(index + 1);
      c[y][number] = c2[x][number] = c3[square(y, x)][number] = false;
      a[y][x] = 0;
    }
  }
}

int main()
{
  for(int i=0; i<9; i++) {
    for(int j=0; j<9; j++) {
      cin >> a[i][j];
      if(a[i][j] != 0) {
        c[i][a[i][j]] = true;
        c2[j][a[i][j]] = true;
        c3[square(i, j)][a[i][j]] = true;
      }
      else {
        zero_pos.push_back(make_pair(i, j));
      }
    }
  }

  go(0);
  return 0;
}