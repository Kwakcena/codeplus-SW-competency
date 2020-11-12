#include <iostream>
#include <vector>
#include <cstring>
#include <string>
#include <tuple>
#include <deque>
#include <queue>
#include <map>
#include <algorithm>

using namespace std;

int n, k;
const int MAX = 200001;
int check[MAX];
map<int, int> dist;

void print(int from, int to) {
  if(from != to) {
    print(from, dist[to]);
  }
  cout << to << " ";
}

void bfs()
{
  queue<int> q;
  q.push(n);
  memset(check, -1, sizeof(check));
  check[n] = 0;

  while (!q.empty())
  {
    int now = q.front();
    if (now == k)
    {
      break;
    }
    q.pop();

    if (now - 1 >= 0 && check[now - 1] == -1)
    {
      q.push(now - 1);
      dist[now - 1] = now;
      check[now - 1] = check[now] + 1;
    }

    if (now + 1 < MAX && check[now + 1] == -1)
    {
      q.push(now + 1);
      dist[now + 1] = now;
      check[now + 1] = check[now] + 1;
    }

    if (now * 2 <= MAX && check[now * 2] == -1)
    {
      q.push(now * 2);
      dist[now * 2] = now;
      check[now * 2] = check[now] + 1;
    }
  }
}

int main()
{
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> n >> k;
  bfs();

  cout << check[k] << endl;
  print(n, k);
  return 0;
}