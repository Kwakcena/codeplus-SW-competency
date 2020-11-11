#include <iostream>
#include <string>
#include <vector>

using namespace std;

int dy[] = {-1, 1, 0, 0};
int dx[] = {0, 0, -1, 1};

int go(vector<string> &board, vector<bool> &check, int y, int x)
{
  int ans = 0;
  for (int i = 0; i < 4; i++)
  {
    int ny = y + dy[i];
    int nx = x + dx[i];

    if (0 <= ny && ny < board.size() && 0 <= nx && nx < board[0].size())
    {
      if (check[board[ny][nx] - 'A'] == false)
      {
        check[board[ny][nx] - 'A'] = true;
        int next = go(board, check, ny, nx);
        if(ans < next) {
          ans = next;
        }
        check[board[ny][nx] - 'A'] = false;
      }
    }
  }
  return ans + 1;
}

int main()
{
  int r, c;
  cin >> r >> c;
  vector<string> board(r);
  for (int i = 0; i < r; i++)
  {
    cin >> board[i];
  }
  vector<bool> check(26);
  check[board[0][0] - 'A'] = true;
  cout << go(board, check, 0, 0) << "\n";
  return 0;
}