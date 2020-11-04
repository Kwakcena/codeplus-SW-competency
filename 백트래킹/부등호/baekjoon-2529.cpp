#include<iostream>
#include<vector>
#include<string>
#include<tuple>
#include<deque>
#include<queue>
#include<algorithm>

using namespace std;

int k;
bool check[10];
char oper[10];
vector<string> ans;

bool ok(string num) {
  for(int i=0; i<k; i++) {
    if(oper[i] == '<' && (int)num[i] > (int)num[i + 1]) return false;
    if(oper[i] == '>' && (int)num[i] < (int)num[i + 1]) return false;
  }
  return true;
}

void go(int index, string num) {
  if(index == k + 1) {
    if(ok(num)) {
      ans.push_back(num);
    }
    return;
  }
  for(int i=0; i<=9; i++) {
    if(check[i]) continue;
    check[i] = true;
    go(index + 1, num+to_string(i));
    check[i] = false;
  }
}
int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  
  cin >> k;
  string num;
  for(int i = 0; i < k; i++) {
    cin >> oper[i];  
  }

  go(0, num);
  cout << ans[0] << endl;
  cout << ans[ans.size() - 1] << endl;
  return 0;
}