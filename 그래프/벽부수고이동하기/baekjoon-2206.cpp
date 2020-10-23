#include<iostream>
#include<cstdio>
#include<cstring>
#include<vector>
#include<tuple>
#include<deque>
#include<queue>
#include<algorithm>

using namespace std;

int map[1000][1000];
int dist[1000][1000][2];
int dy[] = { -1, 1, 0, 0 }, dx[] = { 0, 0, -1, 1 };

int main() {
  int n, m;
  scanf("%d%d", &n, &m);

  for(int i=0; i<n; i++) {
    for(int j=0; j<m; j++) {
      scanf("%1d", &map[i][j]);
    }
  }

  queue<tuple<int, int, int>> q;
  dist[0][0][0] = 1;
  q.push(make_tuple(0, 0, 0));

  while(!q.empty()) {
    int y, x, z;
    tie(y, x, z) = q.front();
    q.pop();

    for(int i=0; i<4; i++) {
      int ny = y + dy[i], nx = x + dx[i];
      
      if(ny < 0 || ny >= n || nx < 0 || nx >= m) continue;
      if(map[ny][nx] == 0 && dist[ny][nx][z] == 0) {
        dist[ny][nx][z] = dist[y][x][z] + 1;
        q.push(make_tuple(ny, nx, z));
      }
      if(z == 0 && map[ny][nx] == 1 && dist[ny][nx][z + 1] == 0) {
        dist[ny][nx][z + 1] = dist[y][x][z] + 1;
        q.push(make_tuple(ny, nx, z + 1));
      }
    }
  }

  if(dist[n-1][m-1][0] != 0 && dist[n-1][m-1][1] != 0) {
    cout << min(dist[n-1][m-1][0], dist[n-1][m-1][1]);
  }
  else if (dist[n-1][m-1][0] != 0) {
    cout << dist[n-1][m-1][0];
  }
  else if (dist[n-1][m-1][1] != 0) {
    cout << dist[n-1][m-1][1];
  }
  else {
    cout << -1;
  }
  cout << '\n';

  return 0;
}