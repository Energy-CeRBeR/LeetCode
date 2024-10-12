#include <vector>
#include <string>

using namespace std;

class Solution
{
public:
    vector<string> fullJustify(vector<string> &words, int maxWidth)
    {
        vector<pair<vector<string>, int>> strings = this->greedy_fill(words, maxWidth);

        vector<string> response;
        for (int i = 0; i < strings.size() - 1; ++i)
        {
            vector<string> data = strings[i].first;
            int length = data.size();
            int count = strings[i].second;
            string cur_string = data[0];

            int space_places = length - 1;
            if (space_places == 0)
            {
                cur_string.append(count, ' ');
                response.push_back(cur_string);
                continue;
            }

            int count_spaces = count / space_places;
            int ost_spaces = count - (count_spaces * space_places);

            for (int i = 1; i < length; ++i)
            {
                cur_string.append(count_spaces, ' ');
                if (ost_spaces)
                {
                    cur_string += ' ';
                    ost_spaces--;
                }
                cur_string += data[i];
            }

            response.push_back(cur_string);
        }

        vector<string> data = strings[strings.size() - 1].first;
        int length = data.size();
        int count = strings[strings.size() - 1].second;

        string cur_string;
        for (int i = 0; i < length - 1; ++i)
        {
            cur_string += data[i] + ' ';
        }

        cur_string += data[length - 1];
        cur_string.append(count - length + 1, ' ');
        response.push_back(cur_string);

        return response;
    }

    vector<pair<vector<string>, int>> greedy_fill(vector<string> &words, int maxWidth)
    {
        int n = words.size();

        vector<pair<vector<string>, int>> result;
        vector<string> cur_data = {words[0]};
        int cur_size = words[0].size();
        for (int i = 1; i < n; ++i)
        {
            string word = words[i];
            if (cur_size + 1 + word.size() <= maxWidth)
            {
                cur_data.push_back(word);
                cur_size += 1 + word.size();
            }
            else
            {
                result.push_back({cur_data, maxWidth - (cur_size - cur_data.size() + 1)});
                cur_data = {word};
                cur_size = word.size();
            }
        }

        if (cur_size)
            result.push_back({cur_data, maxWidth - (cur_size - cur_data.size() + 1)});

        return result;
    }
};