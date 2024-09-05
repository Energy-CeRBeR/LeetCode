#include <iostream>
#include <vector>
#include <map>

using namespace std;

class Solution
{
public:
    int equalPairs(vector<vector<int>> &grid)
    {
        map<vector<int>, int> strings;
        for (auto line : grid)
        {
            if (strings.find(line) == strings.end())
            {
                strings[line] = 0;
            }
            strings[line]++;
        }

        int counter = 0;
        int n = grid.size();
        for (int i = 0; i < n; ++i)
        {
            vector<int> cur_column;
            for (int j = 0; j < n; ++j)
            {
                cur_column.push_back(grid[j][i]);
            }
            if (strings.find(cur_column) != strings.end())
            {
                counter += strings[cur_column];
            }
        }

        return counter;
    }
};