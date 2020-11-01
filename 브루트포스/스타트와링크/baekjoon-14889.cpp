#include<cstdio>
#include<cstring>
#include<vector>
#include<tuple>
#include<deque>
#include<queue>
#include<algorithm>

using namespace std;

int main() {
  int n;
  scanf("%d", &n);

  vector<int> p(n);
  for(int i=0; i<n/2; i++) {
    p[i] = 1;
  }
  sort(p.begin(), p.end());

  int s[n][n];
  for(int i=0; i<n; i++) {
    for(int j=0; j<n; j++) {
      scanf("%d", &s[i][j]);
    }
  }

  int ans = 2147483647;
  do {
    vector<int> first, second;
    for(int i=0; i<n; i++) {
      if(p[i] == 0) {
        first.push_back(i);
      }
      else {
        second.push_back(i);
      }
    }

    int one = 0;
    int two = 0;

    for(int i=0; i<n/2; i++) {
      for(int j=0; j<n/2; j++) {
        if(i == j) continue;
        one += s[first[i]][first[j]];
        two += s[second[i]][second[j]];
      }
    }

    int diff = one - two;
    if(diff < 0) diff = -diff;
    if(ans > diff) ans = diff;
  } while(next_permutation(p.begin(), p.end()));

  printf("%d", ans);
  return 0;
}