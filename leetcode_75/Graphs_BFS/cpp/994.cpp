#include <vector>
#include <deque>
#include <set>
#include <algorithm>

using namespace std;

class Solution
{

    int n, m;

    int bfs(deque<vector<int>> &q, vector<vector<int>> &graph, set<pair<int, int>> &visited)
    {
        int count = 0;
        while (!q.empty())
        {
            vector<int> data = q.front();
            q.pop_front();

            int i = data[0];
            int j = data[1];
            int m = data[2];
            int flag = 0;

            visited.insert({i, j});

            if (0 <= i - 1 && i - 1 < this->n && graph[i - 1][j] == 1 && visited.find({i - 1, j}) == visited.end())
            {
                graph[i - 1][j] = 2;
                flag = 1;
                q.push_back({i - 1, j, m + 1});
            }

            if (0 <= i + 1 && i + 1 < this->n && graph[i + 1][j] == 1 && visited.find({i + 1, j}) == visited.end())
            {
                graph[i + 1][j] = 2;
                flag = 1;
                q.push_back({i + 1, j, m + 1});
            }

            if (0 <= j - 1 && j - 1 < this->m && graph[i][j - 1] == 1 && visited.find({i, j - 1}) == visited.end())
            {
                graph[i][j - 1] = 2;
                flag = 1;
                q.push_back({i, j - 1, m + 1});
            }

            if (0 <= j + 1 && j + 1 < this->m && graph[i][j + 1] == 1 && visited.find({i, j + 1}) == visited.end())
            {
                graph[i][j + 1] = 2;
                flag = 1;
                q.push_back({i, j + 1, m + 1});
            }

            count = max(count, m + flag);
        }

        return count;
    }

    pair<deque<vector<int>>, int> get_roots(vector<vector<int>> &grid)
    {
        deque<vector<int>> roots;
        int good_counter = 0;
        for (int i = 0; i < this->n; ++i)
        {
            for (int j = 0; j < this->m; ++j)
            {
                if (grid[i][j] == 1)
                {
                    good_counter++;
                }
                if (grid[i][j] == 2)
                {
                    roots.push_back({i, j, 0});
                }
            }
        }

        return {roots, good_counter};
    }

public:
    int orangesRotting(vector<vector<int>> &grid)
    {
        this->n = grid.size();
        this->m = grid[0].size();

        pair<deque<vector<int>>, int> data = this->get_roots(grid);
        deque<vector<int>> q = data.first;
        int good_counter = data.second;
        if (q.empty())
        {
            return good_counter == 0 ? 0 : -1;
        }

        set<pair<int, int>> visited;
        int result = this->bfs(q, grid, visited);

        for (int i = 0; i < this->n; ++i)
        {
            for (int j = 0; j < this->m; ++j)
            {
                if (grid[i][j] == 1)
                {
                    return -1;
                }
            }
        }
        return result;
    }
};