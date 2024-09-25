/**
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 */
int guess(int num);

class Solution
{
public:
    int guessNumber(int n)
    {
        long long left = 1;
        long long right = n;
        long long num = (left + right) / 2;

        long long response = guess(num);
        while (response != 0)
        {
            if (response == -1)
            {
                right = num - 1;
            }
            else
            {
                left = num + 1;
            }

            num = (left + right) / 2;
            response = guess(num);
        }

        return num;
    }
};