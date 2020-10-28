#include<cstdio>
#include<cstring>
#include<vector>
#include<tuple>
#include<deque>
#include<queue>
#include<algorithm>

using namespace std;

int main() {
  int t;
  scanf("%d", &t);

  while(t--) {
    int m, n, x, y;
    scanf("%d%d%d%d", &m, &n, &x, &y);
    x--; y--;

    bool ok = false;
    for (int year = x; year < n * m; year+=m)
    {
      if (year % n == y)
      {
        printf("%d\n", year + 1);
        ok = true;
        break;
      }
    }
    if(!ok) {
      printf("-1\n");
    }
  }
  return 0;
}