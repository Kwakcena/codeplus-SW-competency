#include<iostream>
#include<vector>
#include<string>
#include<tuple>
#include<deque>
#include<queue>
#include<algorithm>

using namespace std;

int n;
int s[10][10];
int ans[10];
string str;

bool check(int index) {
  int sum = 0;
  for(int i=index; i>=0; i--){
    sum += ans[i];
    if(s[i][index] == 0) {
      if(sum != 0) return false;
    }
    else if(s[i][index] > 0) {
      if(sum <= 0) return false;
    }
    else if(s[i][index] < 0) {
      if(sum >= 0) return false;
    }
  }
  return true;
}

bool go(int index) {
  if(index == n) 
    return true;

  if(s[index][index] == '0') {
    ans[index] = 0;
    return check(index) && go(index + 1);
  }

  for(int i=1; i<=10; i++) {
    ans[index] = i * s[index][index];
    if(check(index) && go(index + 1)) return true;
  }
  return false; 
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  
  cin >> n;
  cin >> str;

  int index = 0;
  for(int i=0; i<n; i++) {
    for(int j=i; j<n; j++) {
      if(str[index] == '+') {
        s[i][j] = 1;
      }
      else if(str[index] == '-') {
        s[i][j] = -1;
      }
      else if(str[index] == '0') {
        s[i][j] = 0;
      }
      index++;
    }
  }

  go(0);
  for(int i=0; i<n; i++) {
    cout << ans[i] << ' ';
  }
  cout << '\n';

  return 0;
}