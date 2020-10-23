#include <cstdio>
#include <cstring>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int map[101][101];
int visited[101][101];

int dy[] = {-1, 1, 0, 0};
int dx[] = {0, 0, -1, 1};

int n, m;

void bfs(int y, int x, int count)
{
  queue<pair<int, int>> q;
  visited[y][x] = count;

  q.push(make_pair(y, x));

  while (!q.empty())
  {
    y = q.front().first;
    x = q.front().second;
    q.pop();

    for (int i = 0; i < 4; i++)
    {
      int ny = y + dy[i];
      int nx = x + dx[i];

      if (0 <= ny && ny < n && 0 <= nx && nx < m)
      {
        if (map[ny][nx] == 1 && visited[ny][nx] == 0)
        {
          q.push(make_pair(ny, nx));
          visited[ny][nx] = visited[y][x] + 1;
        }
      }
    }
  }
}

int main()
{
  scanf("%d %d", &n, &m);

  for (int i = 0; i < n; i++)
  {
    for (int j = 0; j < m; j++)
    {
      scanf("%1d", &map[i][j]);
    }
  }

  bfs(0, 0, 1);
  printf("%d", visited[n - 1][m - 1]);
  return 0;
}