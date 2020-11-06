#include <iostream>
#include <vector>
#include <deque>
#include <utility>

using namespace std;

bool ok(deque<pair<int, int>> a, int p) {
  for(int i=1; i<a.size(); i++) {
    if(a[i].first > p) {
      return true;
    }
  }
  return false;
}

int solution(vector<int> priorities, int location) {
    int answer = 0;
    deque<pair<int, int>> a;
    for(int i=0; i<priorities.size(); i++) {
      a.push_back(make_pair(priorities[i], i));
    }

    while(a.size() != 0) {
      int priority, current;
      tie(priority, current) = a.front();
      if(ok(a, priority)) {
        a.push_back(a.front());
        a.pop_front();
      }
      else {
        if(a.front().second == location) {
          answer++;
          break;
        }
        a.pop_front();
        answer++;
      }
    }
    return answer;
}


int main() {
  vector<int> p1({2, 1, 3, 2});
  cout << solution(p1, 2) << endl;

  vector<int> p2({1, 1, 9, 1, 1, 1});
  cout << solution(p2, 0);
}