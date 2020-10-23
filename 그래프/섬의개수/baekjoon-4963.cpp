#include<cstdio>
#include<cstring>
#include<vector>
#include<queue>
#include<algorithm>

using namespace std;
int visited[50][50];
int map[50][50];

int dy[] = { -1, 1, 0, 0, -1, 1, -1, 1};
int dx[] = { 0, 0, -1, 1, -1, -1, 1, 1};
int w, h;

void dfs(int y, int x, int land) {
  visited[y][x] = land;

  for(int i=0; i<8; i++) {
    int ny = y + dy[i];
    int nx = x + dx[i];

    if(ny >= 0 && ny < h && nx >= 0 && nx < w) {
      if(visited[ny][nx] == false && map[ny][nx] == 1) {
        dfs(ny, nx, land);
      }
    }
  }
}

int main() {

  while(true) {
    scanf("%d%d", &w, &h);
    if(w == 0 && h == 0) {
      break;
    }

    memset(map, 0, sizeof(map));
    memset(visited, false, sizeof(visited));
    for(int i=0; i<h; i++) {
      for(int j=0; j<w; j++) {
        scanf("%d", &map[i][j]);
      }
    }

    int land = 0;
    for(int i=0; i<h; i++) {
      for(int j=0; j<w; j++) {
        if(visited[i][j] == 0 && map[i][j] == 1) {
          land++;
          dfs(i, j, land);
        }
      }
    }
    
    printf("%d\n", land);
  }


  return 0;
}