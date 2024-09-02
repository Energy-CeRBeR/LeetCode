#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution
{
public:
    int longestOnes(vector<int> &nums, int k)
    {
        vector<int> zeros_indexes;
        int prev_zero = 0;
        int zeros_counter = 0;

        int ind = 0;
        while (ind < nums.size())
        {
            if (nums[ind] == 0)
            {
                zeros_indexes.push_back(ind);
                zeros_counter++;
                if (zeros_counter > k)
                {
                    break;
                }
            }
            ind++;
        }
        int mx = ind;
        zeros_counter--;

        for (int i = ind + 1; i < nums.size(); ++i)
        {
            if (nums[i] != 0)
            {
                mx = max(mx, i - zeros_indexes[prev_zero]);
            }
            else
            {
                zeros_indexes.push_back(i);
                zeros_counter += 1;
                mx = max(mx, i - zeros_indexes[prev_zero] - 1);
                prev_zero++;
                zeros_counter--;
            }
        }

        return mx;
    }
};