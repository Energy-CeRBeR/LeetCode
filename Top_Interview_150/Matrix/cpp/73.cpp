#include <vector>
#include <unordered_set>

using namespace std;

class Solution
{

    void set_null_line(vector<vector<int>> &matrix, int x, int m)
    {
        for (int i = 0; i < m; ++i)
            matrix[x][i] = 0;
    }

    void set_null_column(vector<vector<int>> &matrix, int y, int n)
    {
        for (int i = 0; i < n; ++i)
            matrix[i][y] = 0;
    }

public:
    void setZeroes(vector<vector<int>> &matrix)
    {
        int n = matrix.size();
        int m = matrix[0].size();
        unordered_set<int> null_lines;
        unordered_set<int> null_columns;

        for (int i = 0; i < n; ++i)
        {
            for (int j = 0; j < m; ++j)
            {
                if (matrix[i][j] == 0)
                {
                    null_lines.insert(i);
                    null_columns.insert(j);
                }
            }
        }

        for (int x : null_lines)
            this->set_null_line(matrix, x, m);

        for (int y : null_columns)
            this->set_null_column(matrix, y, n);
    }
};