#include<cstdio>
#include<cstring>
#include<vector>
#include<deque>
#include<queue>
#include<algorithm>

using namespace std;

const int MAX = 200000;

int main() {
  int n, k;
  int time[MAX] = {};
  memset(time, -1, sizeof(time));

  scanf("%d%d", &n, &k);

  deque<int> dq;
  dq.push_back(n);
  time[n] = 0;
  
  while(!dq.empty()) {
    int now = dq.front();
    dq.pop_front();

    if(now == k) {
      break;
    }

    if(now * 2 <= MAX) {
      if(time[now * 2] == -1) {
        dq.push_front(now * 2);
        time[now * 2] = time[now];
      }
    }
    if(now + 1 <= MAX) {
      if(time[now + 1] == -1) {
        dq.push_back(now + 1);
        time[now + 1] = time[now] + 1;
      }
    }
    if(now - 1 >= 0) {
      if(time[now - 1] == -1) {
        dq.push_back(now - 1);
        time[now - 1] = time[now] + 1;
      }
    }
  }
  printf("%d", time[k]);
  return 0;
}