#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <string>

using namespace std;

class Solution
{
public:
    vector<double> calcEquation(vector<vector<string>> &equations, vector<double> &values, vector<vector<string>> &queries)
    {
        unordered_map<string, vector<pair<string, double>>> graph;
        double val;
        string a, b;
        for (int i = 0; i < values.size(); ++i)
        {
            a = equations[i][0];
            b = equations[i][1];
            val = values[i];
            graph[a].push_back(make_pair(b, val));
            graph[b].push_back(make_pair(a, 1 / val));
        }

        vector<double> response;
        string start, finish;
        for (auto query : queries)
        {
            this->cur_res = -1;
            start = query[0];
            finish = query[1];
            unordered_set<string> visited;
            this->dfs(start, finish, graph, visited, 1.0, 1.0);
            response.push_back(this->cur_res);
        }

        return response;
    }

private:
    double cur_res;

    void dfs(string &node,
             string &finish_node,
             unordered_map<string, vector<pair<string, double>>> &graph,
             unordered_set<string> &visited,
             double data,
             double result)
    {
        if (graph.find(node) != graph.end())
        {
            visited.insert(node);
            result *= data;
            if (node == finish_node)
            {
                this->cur_res = result;
                return;
            }

            for (auto v : graph[node])
            {
                if (visited.find(v.first) == visited.end())
                {
                    this->dfs(v.first, finish_node, graph, visited, v.second, result);
                }
            }
        }
    }
};