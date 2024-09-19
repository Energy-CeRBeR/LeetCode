#include <vector>
#include <unordered_map>

using namespace std;

class Solution
{
public:
    int minReorder(int n, vector<vector<int>> &connections)
    {
        unordered_map<int, vector<int>> base_graph;
        unordered_map<int, vector<int>> oriented_graph;
        for (int i = 0; i < n - 1; ++i)
        {
            base_graph[connections[i][0]].push_back(connections[i][1]);
            oriented_graph[connections[i][0]].push_back(connections[i][1]);
            oriented_graph[connections[i][1]].push_back(connections[i][0]);
        }

        int root = 0;
        vector<bool> visited(n, false);
        visited[0] = true;
        this->dfs(root, oriented_graph, base_graph, visited);

        return this->count;
    }

private:
    int count = 0;
    void dfs(
        int node,
        unordered_map<int, vector<int>> &oriented_graph,
        unordered_map<int, vector<int>> &base_graph,
        vector<bool> &visited)
    {
        visited[node] = true;
        for (auto v : oriented_graph[node])
        {
            if (!visited[v])
            {
                if (find(base_graph[node].begin(), base_graph[node].end(), v) != base_graph[node].end())
                {
                    this->count++;
                }
                this->dfs(v, oriented_graph, base_graph, visited);
            }
        }
    }
};