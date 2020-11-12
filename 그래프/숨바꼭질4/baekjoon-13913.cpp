#include <iostream>
#include <queue>

using namespace std;

const int MAX = 200001;
int n, k;
bool check[MAX];
int dist[MAX];
int from[MAX];

void print(int n, int m) {
  if(n != m) {
    print(n, from[m]);
  }
  cout << m << " ";
}

void bfs()
{
  queue<int> q;
  q.push(n);
  check[n] = true;
  dist[n] = 0;

  while (!q.empty())
  {
    int now = q.front();
    if (now == k)
    {
      break;
    }
    q.pop();

    if (now - 1 >= 0 && check[now - 1] == false)
    {
      q.push(now - 1);
      dist[now - 1] = dist[now] + 1;
      check[now - 1] = true;
      from[now - 1] = now;
    }

    if (now + 1 < MAX && check[now + 1] == false)
    {
      q.push(now + 1);
      dist[now + 1] = dist[now] + 1;
      check[now + 1] = true;
      from[now + 1] = now;
    }

    if (now * 2 <= MAX && check[now * 2] == false)
    {
      q.push(now * 2);
      dist[now * 2] = dist[now] + 1;
      check[now * 2] = true;
      from[now * 2] = now;
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

  cout << dist[k] << endl;
  print(n, k);
  return 0;
}