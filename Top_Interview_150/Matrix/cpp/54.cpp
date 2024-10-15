#include <vector>

using namespace std;

class Solution
{
public:
    vector<int> spiralOrder(vector<vector<int>> &matrix)
    {
        int m = matrix.size();
        int n = matrix[0].size();

        vector<int> result;
        int left = 0, up = 1, right = n, down = m;
        int i = 0, j = -1;
        while (result.size() < m * n)
        {
            j++;
            while (result.size() < m * n && j < right)
                result.push_back(matrix[i][j++]);
            j--;
            right--;

            i++;
            while (result.size() < m * n && i < down)
                result.push_back(matrix[i++][j]);
            i--;
            down--;

            j--;
            while (result.size() < m * n && j >= left)
                result.push_back(matrix[i][j--]);
            j++;
            left++;

            i--;
            while (result.size() < m * n && i >= up)
                result.push_back(matrix[i--][j]);
            i++;
            up++;
        }

        return result;
    }
};