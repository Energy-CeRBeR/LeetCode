#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

class Solution
{
public:
    string reverseWords(string s)
    {
        vector<string> lst;
        auto last_symbol = s[s.size() - 1];
        string cur_s;
        if (last_symbol != ' ')
        {
            cur_s += last_symbol;
        }
        for (int i = s.size() - 2; i >= 0; --i)
        {
            if (s[i] != ' ')
            {
                cur_s += s[i];
            }
            else
            {
                if (last_symbol != ' ')
                {
                    lst.push_back(cur_s);
                    cur_s = "";
                }
            }
            last_symbol = s[i];
        }

        if (!cur_s.empty())
        {
            lst.push_back(cur_s);
        }

        string result;
        for (int i = lst.size() - 1; i >= 0; --i)
        {
            result += lst[i] + " ";
        }

        result.pop_back();
        reverse(result.begin(), result.end());

        return result;
    }
};

int main()
{
    Solution solution; // Создаем объект класса Solution
    string s = "a good   example";
    string reversed_string = solution.reverseWords(s); // Вызываем функцию
    cout << reversed_string << endl;                   // Вывод: contest LeetCode take Let's
    return 0;
}