#include <vector>
#include <unordered_set>

using namespace std;

class Solution
{

    bool add_elem(unordered_set<char> &data, char elem)
    {
        int cur_len = data.size();
        data.insert(elem);

        return cur_len != data.size();
    }

public:
    bool isValidSudoku(vector<vector<char>> &board)
    {
        vector<unordered_set<char>> lines(9);
        vector<unordered_set<char>> columns(9);
        vector<vector<unordered_set<char>>> blocks(9, vector<unordered_set<char>>(9));

        unordered_set<char> digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'};

        for (int i = 0; i < 9; ++i)
        {
            for (int j = 0; j < 9; ++j)
            {
                if (digits.find(board[i][j]) != digits.end())
                {
                    bool x1 = this->add_elem(lines[i], board[i][j]);
                    bool x2 = this->add_elem(columns[j], board[i][j]);
                    bool x3 = this->add_elem(blocks[i / 3][j / 3], board[i][j]);

                    if (!(x1 && x2 && x3))
                        return false;
                }
            }
        }

        return true;
    }
};