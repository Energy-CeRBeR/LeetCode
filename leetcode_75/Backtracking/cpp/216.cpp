#include <vector>

using namespace std;

class Solution
{

    vector<vector<int>> result;
    int k;

    void backtracking(int start, vector<int> path, int target)
    {
        if (path.size() == this->k && target == 0)
        {
            this->result.push_back(path);
            return;
        }

        if (path.size() >= this->k || target < 0)
        {
            return;
        }

        for (int i = start; i < 10; ++i)
        {
            path.push_back(i);
            backtracking(i + 1, path, target - i);
            path.pop_back();
        }
    }

public:
    vector<vector<int>> combinationSum3(int k, int n)
    {
        this->k = k;
        this->backtracking(1, {}, n);

        return this->result;
    }
};