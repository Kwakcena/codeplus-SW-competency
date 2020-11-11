#include <iostream>

using namespace std;

int r, c;
char a[21][21];
bool check[150];

int dy[] = {-1, 1, 0, 0};
int dx[] = {0, 0, -1, 1};

int ans;

void go(int y, int x, int count)
{
  if (ans < count)
  {
    ans = count;
  }

  for (int i = 0; i < 4; i++)
  {
    int ny = y + dy[i];
    int nx = x + dx[i];

    if (0 <= ny && ny < r && 0 <= nx && nx < c)
    {
      if (check[a[ny][nx]] == false)
      {
        check[a[ny][nx]] = true;
        go(ny, nx, count + 1);
        check[a[ny][nx]] = false;
      }
    }
  }
}

int main()
{
  cin >> r >> c;
  for (int i = 0; i < r; i++)
  {
    for (int j = 0; j < c; j++)
    {
      cin >> a[i][j];
    }
  }

  check[a[0][0]] = true;
  go(0, 0, 1);
  cout << ans;
  return 0;
}