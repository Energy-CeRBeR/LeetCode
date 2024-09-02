#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution
{
public:
    int longestSubarray(vector<int> &nums)
    {
        int INF = nums.size() + 1;
        vector<int> two_last_zeros_indexes;
        int size = nums.size();
        int ind = 0;

        while (ind < size)
        {
            if (nums[ind] == 0)
            {
                two_last_zeros_indexes.push_back(ind);
                if (two_last_zeros_indexes.size() == 2)
                {
                    break;
                }
            }
            ind++;
        }

        if (two_last_zeros_indexes.size() < 2)
        {
            return size - 1;
        }

        int mx = ind - 1;
        int start_pos = two_last_zeros_indexes[0] + 1;
        for (int i = ind + 1; i < size; ++i)
        {
            if (nums[i] == 0)
            {
                mx = max(mx, i - start_pos - 1);
                two_last_zeros_indexes[0] = two_last_zeros_indexes[1];
                two_last_zeros_indexes[1] = i;
                start_pos = two_last_zeros_indexes[0] + 1;
            }
            else
            {
                mx = max(mx, i - start_pos);
            }
        }

        return mx;
    }
};