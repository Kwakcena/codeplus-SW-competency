#include<iostream>
#include<vector>
#include<cstring>
#include<string>
#include<tuple>
#include<deque>
#include<queue>
#include<algorithm>

using namespace std;

const int MAX = 10000;
int from[MAX];
char how[MAX];
int dist[MAX];

void print(int n, int m) {
  if(n == m) return;
  print(n, from[m]);
  cout << how[m];
}

void check(int now, int next, char c, queue<int> &q) {
  if(dist[next] == -1) {
    q.push(next);
    dist[next] = dist[now] + 1;
    from[next] = now;
    how[next] = c;
  }
}

void bfs(int a, int b) {
  queue<int> q;
  q.push(a);
  
  memset(dist, -1, sizeof(dist));
  memset(from, -1, sizeof(from));
  memset(how, 0, sizeof(how));

  dist[a] = 0;
  while(!q.empty()) {
    int now = q.front();
    q.pop();

    int next;
    next = (now * 2) % MAX;
    check(now, next, 'D', q);

    next = now - 1;
    if(next == -1) next = 9999;
    check(now, next, 'S', q);

    next = (now % 1000) * 10 + now / 1000;
    check(now, next, 'L', q);

    next = (now / 10) + (now % 10) * 1000;
    check(now, next, 'R', q);
  }
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  
  int t;
  cin >> t;
  for(int i=0; i<t; i++) {
    int a, b;
    cin >> a >> b;
    bfs(a, b);
    print(a, b);
    cout << '\n';
  }
  return 0;
}