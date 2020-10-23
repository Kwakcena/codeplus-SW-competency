#include<cstdio>
#include<cstring>
#include<vector>
#include<queue>
#include<algorithm>

using namespace std;

void dfs(int x, bool visited[], vector<int> adj[]) {
  visited[x] = true;

  for(int next : adj[x]) {
    if(!visited[next]) {
      dfs(next, visited, adj);
    }
  }
}

int main() {
  int n, m;
  scanf("%d%d", &n, &m);

  vector<int> adj_list[n + 1];
  bool visited[n + 1];
  memset(visited, false, sizeof(visited));

  for (size_t i = 0; i < m; i++)
  {
    int from, to;
    scanf("%d%d", &from, &to);
    
    adj_list[from].push_back(to);
    adj_list[to].push_back(from);
  }


  int ans = 0;
  for (size_t i = 1; i <= n; i++)
  {
    if(!visited[i]) {
      dfs(i, visited, adj_list);
      ans++;
    }
  }
  
  printf("%d", ans);
  
  return 0;
}