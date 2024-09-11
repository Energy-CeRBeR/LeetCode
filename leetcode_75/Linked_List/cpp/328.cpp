struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution
{
public:
    ListNode *oddEvenList(ListNode *head)
    {
        ListNode *odd_head = nullptr;
        ListNode *even_head = nullptr;
        ListNode *cur_odd_obj = nullptr;
        ListNode *cur_even_obj = nullptr;
        ListNode *cur_obj = head;
        ListNode *next_obj = nullptr;
        int cur_ind = 1;

        while (cur_obj != nullptr)
        {
            next_obj = cur_obj->next;
            cur_obj->next = nullptr;
            if (cur_ind % 2 != 0)
            {
                if (odd_head != nullptr)
                {
                    cur_odd_obj->next = cur_obj;
                }
                else
                {
                    odd_head = cur_obj;
                }
                cur_odd_obj = cur_obj;
            }
            else
            {
                if (even_head != nullptr)
                {
                    cur_even_obj->next = cur_obj;
                }
                else
                {
                    even_head = cur_obj;
                }
                cur_even_obj = cur_obj;
            }

            cur_obj = next_obj;
            cur_ind++;
        }

        if (cur_odd_obj != nullptr)
        {
            cur_odd_obj->next = even_head;
        }

        return odd_head;
    }
};