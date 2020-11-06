#include <iostream>
#include <vector>
#include <string>
#include <tuple>
#include <deque>
#include <queue>
#include <algorithm>

using namespace std;

int k;
bool check[10];
char oper[10];
vector<string> ans;

bool good(char current_number, char next_number, char op)
{
  if (op == '<')
  {
    if (current_number > next_number)
      return false;
  }
  if (op == '>')
  {
    if (current_number < next_number)
      return false;
  }
  return true;
}

void go(int index, string num)
{
  if (index == k + 1)
  {
    ans.push_back(num);
    return;
  }
  for (int i = 0; i <= 9; i++)
  {
    if (check[i])
      continue;
    if (index == 0 || good(num[index - 1], i + '0', oper[index - 1]))
    {
      check[i] = true;
      go(index + 1, num + to_string(i));
      check[i] = false;
    }
  }
}

int main()
{
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> k;
  string num;
  for (int i = 0; i < k; i++)
  {
    cin >> oper[i];
  }

  go(0, num);

  cout << ans[ans.size() - 1] << endl;
  cout << ans[0] << endl;
  return 0;
}