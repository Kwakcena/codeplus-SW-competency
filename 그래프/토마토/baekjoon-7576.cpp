#include <cstdio>
#include <cstring>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int tomato[1001][1001];
bool visited[1001][1001];

int dy[] = {-1, 1, 0, 0};
int dx[] = {0, 0, -1, 1};

int m, n;

vector<pair<int, int>> tomato_pos;

void bfs()
{
  queue<pair<int, int>> q;

  for (pair<int, int> pos : tomato_pos)
  {
    int pos_y = pos.first, pos_x = pos.second;
    visited[pos_y][pos_x] = true;
    q.push(pos);
  }

  while (!q.empty())
  {
    int now_y = q.front().first, now_x = q.front().second;
    q.pop();

    for (int i = 0; i < 4; i++)
    {
      int next_y = now_y + dy[i], next_x = now_x + dx[i];
      if (0 <= next_y && next_y < n && 0 <= next_x && next_x < m)
      {
        if (!visited[next_y][next_x] && tomato[next_y][next_x] == 0)
        {
          q.push(make_pair(next_y, next_x));
          tomato[next_y][next_x] = tomato[now_y][now_x] + 1;
          visited[next_y][next_x] = true;
        }
      }
    }
  }
}

int main()
{
  scanf("%d%d", &m, &n);

  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      scanf("%d", &tomato[i][j]);
      if (tomato[i][j] == 1) {
        tomato_pos.push_back(make_pair(i, j));
      }
    }
  }

  bfs();

  int ans = -1;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      if(tomato[i][j] == 0) {
        ans = -1;
        break;
      }
      else if(tomato[i][j] > ans) {
        ans = tomato[i][j];
      }
    }
    if(ans == -1) {
      break;
    }
  }

  printf("%d", ans == -1 ? -1 : ans - 1);
  return 0;
}