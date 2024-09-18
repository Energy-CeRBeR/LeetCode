#include <vector>
#include <unordered_map>

using namespace std;

class Solution
{
public:
    int findCircleNum(vector<vector<int>> &isConnected)
    {
        int n = isConnected.size();
        unordered_map<int, vector<int>> graph;
        for (int i = 1; i < n + 1; ++i)
        {
            for (int j = 1; j < isConnected[i].size() + 1; ++j)
            {
                if (isConnected[i - 1][j - 1] && i != j)
                {
                    graph[i].push_back(j);
                    graph[j].push_back(i);
                }
            }
        }

        vector<bool> visited(n + 1, false);
        int count = 0;
        for (int i = 1; i < n + 1; ++i)
        {
            if (!visited[i])
            {
                this->dfs(i, graph, visited);
                count++;
            }
        }

        return count;
    }

private:
    void dfs(int node, unordered_map<int, vector<int>> &graph, vector<bool> &visited)
    {
        visited[node] = true;

        for (auto v : graph[node])
        {
            if (!visited[v])
            {
                this->dfs(v, graph, visited);
            }
        }
    }
};