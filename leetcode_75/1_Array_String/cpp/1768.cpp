#include <iostream>
#include <string>

using namespace std;

class Solution
{
public:
    string mergeAlternately(string word1, string word2)
    {
        string result;
        int l1 = word1.size();
        int l2 = word2.size();
        int ptr1 = 0;
        int ptr2 = 0;
        while (ptr1 < l1 || ptr2 < l2)
        {
            if (ptr1 < l1)
            {
                result += word1[ptr1];
                ptr1++;
            }
            if (ptr2 < l2)
            {
                result += word2[ptr2];
                ptr2++;
            }
        }
        return result;
    }
};