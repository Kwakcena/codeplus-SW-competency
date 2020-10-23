#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

vector<int> edge[2001];

bool dfs(int x, int count, bool check[])
{
  check[x] = true;

  if (count == 4)
  {
    return true;
  }

  for (int y : edge[x])
  {
    if (!check[y])
    {
      if (dfs(y, count + 1, check))
      {
        return true;
      }
      else
      {
        check[y] = false;
      }
    }
  }
  return false;
}

int main()
{
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  int n, m;
  cin >> n >> m;

  for (size_t i = 0; i < m; i++)
  {
    int a, b;
    cin >> a >> b;

    edge[a].push_back(b);
    edge[b].push_back(a);
  }

  bool ans = false;
  for (size_t x = 0; x < n; x++)
  {
    bool check[2001] = {false};

    if (dfs(x, 0, check))
    {
      ans = true;
      break;
    }
  }

  cout << (ans ? 1 : 0) << endl;

  return 0;
}