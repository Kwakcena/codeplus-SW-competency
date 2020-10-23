#include <cstdio>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

vector<int> adj_list[10001];
bool check[10001];

void dfs(int x)
{
  check[x] = true;
  printf("%d ", x);

  for (int y : adj_list[x])
  {
    if (!check[y])
    {
      dfs(y);
    }
  }
}

void bfs(int x)
{
  bool visited[10001] = {false};
  queue<int> q;

  visited[x] = true;
  q.push(x);

  while (!q.empty())
  {
    int now = q.front();
    q.pop();
    printf("%d ", now);

    for (int next : adj_list[now])
    {
      if (!visited[next])
      {
        visited[next] = true;
        q.push(next);
      }
    }
  }
}

int main()
{
  int n, m, v;
  scanf("%d%d%d", &n, &m, &v);

  for (size_t i = 0; i < m; i++)
  {
    int from, to;
    scanf("%d%d", &from, &to);
    adj_list[from].push_back(to);
    adj_list[to].push_back(from);
  }

  for (size_t i = 0; i < m; i++)
  {
    sort(adj_list[i].begin(), adj_list[i].end());
  }

  dfs(v);
  printf("\n");
  bfs(v);

  return 0;
}