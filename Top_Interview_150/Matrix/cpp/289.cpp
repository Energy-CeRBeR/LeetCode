#include <vector>
#include <set>

using namespace std;

class Solution
{
public:
    void gameOfLife(vector<vector<int>> &board)
    {
        set<pair<int, int>> directions = {
            {1, 0},
            {1, -1},
            {0, -1},
            {-1, -1},
            {-1, 0},
            {-1, 1},
            {0, 1},
            {1, 1}};

        int n = board.size();
        int m = board[0].size();

        for (int i = 0; i < n; ++i)
        {
            for (int j = 0; j < m; ++j)
            {
                int live = 0;
                for (auto &d : directions)
                {
                    int x = d.first, y = d.second;
                    if ((i + x < n && i + x >= 0) &&
                        (j + y < m && j + y >= 0) &&
                        abs(board[i + x][j + y]) == 1)
                    {
                        live++;
                    }
                }

                if (board[i][j] == 1 && (live < 2 || live > 3))
                {
                    board[i][j] = -1;
                }

                if (board[i][j] == 0 && live == 3)
                {
                    board[i][j] = 2;
                }
            }
        }

        for (int i = 0; i < n; ++i)
        {
            for (int j = 0; j < m; ++j)
            {
                board[i][j] = (board[i][j] > 0) ? 1 : 0;
            }
        }
    }
};