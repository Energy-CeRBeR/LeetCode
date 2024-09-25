#include <vector>
#include <algorithm>

using namespace std;

class Solution
{

    int n;

    int binary_check_counter(vector<int> &arr, long long coeff, long long target)
    {
        int left = 0;
        int right = this->n - 1;
        int mid;
        while (left <= right)
        {
            mid = (left + right) / 2;
            if (arr[mid] * coeff >= target)
            {
                right = mid - 1;
            }
            else
            {
                left = mid + 1;
            }
        }

        return this->n - left;
    }

public:
    vector<int> successfulPairs(vector<int> &spells, vector<int> &potions, long long success)
    {
        this->n = potions.size();

        sort(potions.begin(), potions.end());

        vector<int> result(spells.size());
        for (int i = 0; i < spells.size(); ++i)
        {
            result[i] = this->binary_check_counter(potions, spells[i], success);
        }

        return result;
    }
};