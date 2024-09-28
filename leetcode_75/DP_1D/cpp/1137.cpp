class Solution
{
public:
    int tribonacci(int n)
    {
        if (n == 0)
        {
            return 0;
        }

        if (n < 3)
        {
            return 1;
        }

        int prev_1, prev_2, prev_3, cur;
        prev_1 = 0;
        prev_2 = 1;
        prev_3 = 1;
        cur = 1;

        for (int i = 0; i < n - 2; ++i)
        {
            cur = prev_1 + prev_2 + prev_3;
            prev_1 = prev_2;
            prev_2 = prev_3;
            prev_3 = cur;
        }

        return cur;
    }
};