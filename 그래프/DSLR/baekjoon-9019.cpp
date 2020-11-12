#include<iostream>
#include<vector>
#include<string>
#include<cstring>
#include<tuple>
#include<deque>
#include<queue>
#include<algorithm>

using namespace std;

const int MAX = 10000;

int left_rotate(string &s) {
  rotate(s.begin(), s.begin() + 1, s.end());
  return stoi(s);
}

int right_rotate(string &s) {
  rotate(s.rbegin(), s.rbegin() + 1, s.rend());
  return stoi(s);
}

void print(int n, int m, vector<pair<char, int>> &from) {
  if(n != m) {
    print(n, from[m].second, from);
  }
  cout << from[m].first;
}

void bfs(int a, int b, vector<pair<char, int>> &from) {
  bool check[MAX];
  memset(check, false, sizeof(check));
  
  queue<string> q;
  q.push(to_string(a));
  check[a] = true;

  while(!q.empty()) {
    string s_now = q.front();

    q.pop();
    int i_now = stoi(s_now);
    if(i_now == b) {
      break;
    }
    int next;
    next = i_now * 2 < MAX ? i_now * 2 : (i_now * 2) % MAX;
    if(check[next] == false) {
      check[next] = true;
      from[next] = make_pair('D', i_now);
      q.push(to_string(next));
    }

    next = i_now - 1 > 0 ? i_now -1 : 9999;
    if(check[next] == false) {
      check[next] = true;
      from[next] = make_pair('S', i_now);
      q.push(to_string(next));
    }

    next = left_rotate(s_now);
    if(check[next] == false) {
      check[next] = true;
      from[next] = make_pair('L', i_now);

      q.push(to_string(next));
    }

    next = right_rotate(s_now);
    if(check[next] == false) {
      check[next] = true;
      from[next] = make_pair('R', i_now);

      q.push(to_string(next));
    }
  }
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  
  int t;
  cin >> t;
  for(int i=0; i<t; i++) {
    int a, b;
    cin >> a >> b;
    vector<pair<char, int>> from(MAX);
    bfs(a, b, from);
    print(a, b, from);
    cout << '\n';
  }


  return 0;
}