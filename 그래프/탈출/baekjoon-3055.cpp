#include<cstdio>
#include<cstring>
#include<vector>
#include<tuple>
#include<deque>
#include<queue>
#include<algorithm>

using namespace std;

char map[50][50];
int end_y, end_x;
int start_y, start_x;
int r, c;

int dy[] = { -1, 1, 0, 0 }, dx[] = { 0, 0, -1, 1 };
queue<pair<int, int>> water_pos;

int water_dist[50][50];
int kaktus_dist[50][50];

void water_bfs() {
  queue<pair<int, int>> q(water_pos);
  
  while(!q.empty()) {
    int y, x;
    tie(y, x) = q.front(); q.pop();

    for(int i=0; i<4; i++) {
      int ny = y + dy[i];
      int nx = x + dx[i];

      if(ny < 0 || ny >= r || nx < 0 || nx >= c) continue;
      if(water_dist[ny][nx] == -1) {
        if(map[ny][nx] == 'S' || map[ny][nx] == '.') {
          q.push(make_pair(ny, nx));
          water_dist[ny][nx] = water_dist[y][x] + 1;
        }
      }
    }
  }
}

void kaktus_bfs() {
  queue<pair<int, int>> q;
  q.push(make_pair(start_y, start_x));

  while(!q.empty()) {
    int y, x;
    tie(y, x) = q.front();
    q.pop();

    for(int i=0; i<4; i++) {
      int ny = y + dy[i];
      int nx = x + dx[i];

      if(ny < 0 || ny >= r || nx < 0 || nx >= c) continue;
      if(kaktus_dist[ny][nx] != -1) continue;
      if(map[ny][nx] == 'X') continue;
      if(water_dist[ny][nx] != -1 && kaktus_dist[y][x] + 1 >= water_dist[ny][nx]) continue;

      kaktus_dist[ny][nx] = kaktus_dist[y][x] + 1;
      q.push(make_pair(ny, nx));
    }
  }
}

int main() {
  scanf("%d%d", &r, &c);
  memset(water_dist, -1, sizeof(water_dist));
  memset(kaktus_dist, -1, sizeof(kaktus_dist));

  for(int i=0; i<r; i++) {
    for(int j=0; j<c; j++) {
      scanf(" %c", &map[i][j]);
      if(map[i][j] == 'D') {
        end_y = i, end_x = j;
      }
      else if(map[i][j] == '*') {
        water_pos.push(make_pair(i, j));
        water_dist[i][j] = 0;
      }
      else if(map[i][j] == 'S') {
        start_y = i, start_x = j;
        kaktus_dist[i][j] = 0;
      }
    }
  }

  water_bfs();
  kaktus_bfs();
  
  if(kaktus_dist[end_y][end_x] == -1) {
    printf("KAKTUS");
  }
  else {
    printf("%d", kaktus_dist[end_y][end_x]);
  }
  return 0;
}