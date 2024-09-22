#include <vector>
#include <deque>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

class Solution
{
    int INF = 10000;

    void bfs(
        deque<pair<int, int>> &q,
        map<pair<int, int>, set<pair<int, int>>> &graph,
        map<pair<int, int>, int> &dist)
    {
        while (!q.empty())
        {
            pair<int, int> node = q.front();
            q.pop_front();
            for (auto neighbour : graph[node])
            {
                if (dist[neighbour] == this->INF)
                {
                    q.push_back(neighbour);
                    dist[neighbour] = min(dist[neighbour], dist[node] + 1);
                }
            }
        }
    }

public:
    int nearestExit(vector<vector<char>> &maze, vector<int> &entrance)
    {

        int n = maze.size();
        int m = maze[0].size();

        map<pair<int, int>, set<pair<int, int>>> graph;
        map<pair<int, int>, int> dist;
        set<pair<int, int>> exits;

        for (int i = 0; i < n; ++i)
        {
            for (int j = 0; j < m; ++j)
            {
                if (maze[i][j] == '.')
                {
                    dist[{i, j}] = this->INF;
                    set<pair<int, int>> t;
                    graph[{i, j}] = t;

                    if (i == 0 || i == n - 1 || j == 0 || j == m - 1)
                    {
                        exits.insert({i, j});
                    }

                    if (i - 1 >= 0 && maze[i - 1][j] == '.')
                    {
                        graph[{i, j}].insert({i - 1, j});
                    }
                    if (i + 1 < n && maze[i + 1][j] == '.')
                    {
                        graph[{i, j}].insert({i + 1, j});
                    }
                    if (j - 1 >= 0 && maze[i][j - 1] == '.')
                    {
                        graph[{i, j}].insert({i, j - 1});
                    }
                    if (j + 1 < m && maze[i][j + 1] == '.')
                    {
                        graph[{i, j}].insert({i, j + 1});
                    }
                }
            }
        }

        pair<int, int> root = {entrance[0], entrance[1]};
        dist[root] = 0;
        deque<pair<int, int>> q = {root};

        this->bfs(q, graph, dist);

        int mn = this->INF;
        for (auto pos : exits)
        {
            int d = dist[pos];
            if (d != 0)
            {
                mn = min(mn, d);
            }
        }

        if (mn != this->INF)
        {
            return mn;
        }
        else
        {
            return -1;
        }
    }
};