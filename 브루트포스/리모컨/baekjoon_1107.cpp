#include<cstdio>
#include<cstring>
#include<vector>
#include<tuple>
#include<deque>
#include<queue>
#include<algorithm>

using namespace std;
int n, m;
bool broken[10];

int getButtonCount(int c) {
  if(broken[c]) {
    return 0;
  }

  int len = 0;
  while(c) {
    if(broken[c % 10]) {
      return 0;
    }
    else {
      len++;
      c /= 10;
    }
  }
  return len;
}

int main() {
  scanf("%d%d", &n, &m);
  for(int i=0; i<m; i++) {
    int temp;
    scanf("%d", &temp);
    broken[temp] = true;
  }

  int ans = n - 100;
  if(ans < 0) {
    ans = -ans;
  }

  for (int c = 5450; c <= 5460; c++) {
    int count = getButtonCount(c);
    if(count == 0) continue;

    int temp = n - c;
    if(temp < 0) {
      temp = -temp;
    }

    if(ans > temp + count) {
      ans = temp + count;
    }
  }
  
  printf("%d", ans);
  return 0;
}