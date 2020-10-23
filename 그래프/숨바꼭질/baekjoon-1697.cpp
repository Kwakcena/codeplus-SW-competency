#include<cstdio>
#include<cstring>
#include<vector>
#include<queue>
#include<algorithm>

using namespace std;

const int MAX_LEN = 200000;

int main() {
  int n, k;
  int visited[MAX_LEN] = {};

  scanf("%d%d", &n, &k);

  queue<int> q;
  q.push(n);

  while(!q.empty()) {
    int now = q.front();
    if(now == k) {
      break;
    }
    q.pop();

    if(0 <= now - 1 && visited[now - 1] == 0) {
      q.push(now - 1);
      visited[now - 1] = visited[now] + 1;
    }
    if(now + 1 <= MAX_LEN && visited[now + 1] == 0) {
      q.push(now + 1);
      visited[now + 1] = visited[now] + 1;
    }
    if(now * 2 <= MAX_LEN && visited[now * 2] == 0) {
      q.push(now * 2);
      visited[now * 2] = visited[now] + 1;
    }
  }
  printf("%d", visited[k]);
  return 0;
}