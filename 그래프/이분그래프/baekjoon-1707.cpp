#include <cstdio>
#include <cstring>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int color[20001];
vector<int> adj[20001];

bool bfs(int start)
{
  queue<int> q;
  color[start] = 1;
  q.push(start);

  while (!q.empty())
  {
    int now = q.front();
    q.pop();

    for (int next : adj[now])
    {
      if (color[next] == 0)
      {
        q.push(next);
        color[next] = 3 - color[now];
      }
      else if (color[next] == color[now])
      {
        return false;
      }
    }
  }

  return true;
}

int main()
{
  int testCase;
  scanf("%d", &testCase);

  for (size_t t = 0; t < testCase; t++)
  {
    int v, e;
    scanf("%d%d", &v, &e);

    for (size_t i = 1; i <= v; i++)
    {
      adj[i].clear();
      color[i] = 0;
    }

    for (size_t i = 0; i < e; i++)
    {
      int from, to;
      scanf("%d%d", &from, &to);

      adj[from].push_back(to);
      adj[to].push_back(from);
    }

    bool ans = true;
    for (size_t start = 1; start <= v; start++)
    {
      if (color[start] == 0)
      {
        if (!bfs(start))
        {
          ans = false;
        }
      }
    }

    printf("%s\n", ans ? "YES" : "NO");
  }

  return 0;
}