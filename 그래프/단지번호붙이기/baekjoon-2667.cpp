#include<cstdio>
#include<cstring>
#include<vector>
#include<queue>
#include<algorithm>

using namespace std;

int map[30][30];
int visited[30][30];

int dy[4] = {-1, 1, 0, 0};
int dx[4] = {0, 0, -1, 1};
int n;

void dfs(int y, int x, int number)
{
  visited[y][x] = number;

  for (int i = 0; i < 4; i++)
  {
    int ny = y + dy[i];
    int nx = x + dx[i];

    if(ny >= 0 && ny < n && nx >= 0 && nx < n) {
      if(visited[ny][nx] == 0 && map[ny][nx] == 1) {
        dfs(ny, nx, number);
      }
    }
  }
}

int main() {
  scanf("%d", &n);

  for (int i = 0; i < n; i++)
  {
    for (int j = 0; j < n; j++)
    {
      scanf("%1d", &map[i][j]);
    }
  }

  int number = 1;
  for (int i = 0; i < n; i++)
  {
    for (int j = 0; j < n; j++)
    {
      if(map[i][j] == 1 && visited[i][j] == 0) {
        dfs(i, j, number);
        number++;
      }
    }
  }

  int ans[25*25] = {};

  for (int i = 0; i < n; i++)
  {
    for (int j = 0; j < n; j++)
    {
      ans[visited[i][j]] += 1;
    }
  }

  sort(ans+1, ans+number);
  printf("%d\n", --number);
  for (int i = 1; i <= number; i++)
  {
    printf("%d\n", ans[i]);
  }
  return 0;
}