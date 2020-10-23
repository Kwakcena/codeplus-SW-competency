#include<cstdio>
#include<cstring>
#include<vector>
#include<deque>
#include<queue>
#include<tuple>
#include<algorithm>

using namespace std;

const int MAX = 100;

int dy[] = {-1, 1, 0, 0}, dx[] = {0, 0, -1, 1};
int map[MAX + 1][MAX + 1];
int dist[MAX + 1][MAX + 1];
int m, n;

void bfs() {
  memset(dist, -1, sizeof(dist));

  deque<pair<int, int>> dq;
  dq.push_back({ 0, 0 });
  dist[0][0] = 0;

  while(!dq.empty()) {
    int y, x;
    tie(y, x) = dq.front();
    dq.pop_front();

    for(int i=0; i<4; i++) {
      int ny = y + dy[i], nx = x + dx[i];
      if(0 <= ny && ny < n && 0 <= nx && nx < m) {
        if(map[ny][nx] == 0 && dist[ny][nx] == -1) {
          dq.push_front({ ny, nx });
          dist[ny][nx] = dist[y][x];
        }
        if(map[ny][nx] == 1 && dist[ny][nx] == -1) {
          dq.push_back({ ny, nx });
          dist[ny][nx] = dist[y][x] + 1;
        }
      }
    }
  }
}

// 벽을 안부수고 갈 수 있는 길을 push_front로 담는다.
int main() {
  scanf("%d%d", &m, &n);

  for(int i=0; i<n; i++) {
    for(int j=0; j<m; j++) {
      scanf("%1d", &map[i][j]);
    }
  }

  bfs();
  printf("%d", dist[n - 1][m - 1]);

  return 0;
}