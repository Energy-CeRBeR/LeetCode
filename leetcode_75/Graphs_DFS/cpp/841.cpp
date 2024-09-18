#include <vector>
#include <unordered_map>

using namespace std;

class Solution
{
public:
    bool canVisitAllRooms(vector<vector<int>> &rooms)
    {
        unordered_map<int, vector<int>> graph;
        int n = rooms.size();

        for (int i = 0; i < n; ++i)
        {
            graph[i] = rooms[i];
        }

        vector<bool> visited(n, false);
        int root = 0;
        this->dfs(root, graph, visited);

        for (auto x : visited)
        {
            if (!x)
            {
                return false;
            }
        }
        return true;
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