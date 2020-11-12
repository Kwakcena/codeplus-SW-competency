#include<iostream>
#include<vector>
#include<cstring>
#include<string>
#include<tuple>
#include<deque>
#include<queue>
#include<algorithm>

using namespace std;

int n, k;
const int MAX = 200001;
int check[MAX];
vector<string> dist(MAX);

void bfs() {
  queue<int> q;
  q.push(n);
  memset(check, -1, sizeof(check));
  check[n] = 0;
  dist[n] += to_string(n);

  while(!q.empty()) {
    int now = q.front();
    if(now == k) {
      break;
    }
    q.pop();

    if(now - 1 >= 0 && check[now - 1] == -1) {
      q.push(now - 1);
      dist[now - 1] = dist[now] + ' ' + to_string(now - 1);
      check[now - 1] = check[now] + 1;
    }

    if(now + 1 < MAX && check[now + 1] == -1) {
      q.push(now + 1);
      dist[now + 1] = dist[now] + ' ' + to_string(now + 1);
      check[now + 1] = check[now] + 1;
    }

    if(now * 2 <= MAX && check[now * 2] == -1) {
      q.push(now * 2);
      dist[now * 2] = dist[now] + ' ' + to_string(now * 2);
      check[now * 2] = check[now] + 1;
    }
  }
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  
  cin >> n >> k;
  bfs();

  cout << check[k] << endl;
  cout << dist[k];
  return 0;
}