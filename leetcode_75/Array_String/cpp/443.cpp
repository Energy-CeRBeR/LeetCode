#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution
{
public:
    int compress(vector<char> &chars)
    {
        int counter = 1;
        int counter_index = 1;
        int start_index = 0;
        for (int i = 1; i < chars.size(); ++i)
        {
            if (chars[i] != chars[start_index])
            {
                if (counter > 1)
                {
                    for (auto c : to_string(counter))
                    {
                        chars[counter_index] = c;
                        counter_index++;
                    }
                }
                start_index = i;
                counter = 1;
                counter_index = i + 1;
            }
            else
            {
                chars[i] = ' ';
                counter++;
            }
        }

        if (chars[chars.size() - 1] == ' ')
        {
            for (auto c : to_string(counter))
            {
                chars[counter_index] = c;
                counter_index++;
            }
        }

        for (auto c : chars)
        {
            cout << c << " ";
        }
        cout << endl;

        int ind = 0;
        while (ind < chars.size())
        {
            if (chars[ind] == ' ')
            {
                chars.erase(chars.begin() + ind);
                ind--;
            }
            ind++;
        }

        for (auto c : chars)
        {
            cout << c << " ";
        }
        cout << endl;

        return chars.size();
    }
};