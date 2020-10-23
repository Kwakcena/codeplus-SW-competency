#include<cstdio>
#include<cstring>
#include<vector>
#include<queue>
#include<algorithm>

using namespace std;

const int MAX = 1000;

int main() {
  int n;
  int time[MAX + 1][MAX + 1] = {};

  scanf("%d", &n);

  queue<pair<int, int>> q;
  q.push({ 1, 0 });

  while(!q.empty()) {
    int s = q.front().first;
    int c = q.front().second;
    q.pop();

    if(s == n) {
      break;
    }

    if(time[s][s] == 0) {
      q.push({ s, s });
      time[s][s] = time[s][c] + 1;
    }
    if(s + c <= n) {
      if(time[s + c][c] == 0) {
        q.push({ s + c, c });
        time[s + c][c] = time[s][c] + 1;
      }
    }
    if(s - 1 >= 0) {
      if(time[s - 1][c] == 0) {
        q.push({ s - 1, c });
        time[s - 1][c] = time[s][c] + 1;
      }
    }
  }

  int ans = -1;
  for(int i=0; i<=n; i++) {
    if(time[n][i] != 0) {
      if(ans == -1 || ans > time[n][i]) {
        ans = time[n][i];
      }
    }
  }

  printf("%d\n", ans);
  return 0;
}