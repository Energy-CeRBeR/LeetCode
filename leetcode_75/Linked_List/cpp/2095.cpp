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
    ListNode *deleteMiddle(ListNode *head)
    {
        int n = this->get_length(head);
        if (n == 1)
        {
            return nullptr;
        }
        int middle = n / 2;

        ListNode *prev = nullptr;
        ListNode *cur = head;
        ListNode *next = cur->next;
        int k = 0;
        while (k != middle)
        {
            prev = cur;
            cur = next;
            next = cur->next;
            k++;
        }

        if (next != nullptr)
        {
            prev->next = next;
        }
        else
        {
            prev->next = nullptr;
        }

        return head;
    }

private:
    int get_length(ListNode *head)
    {
        ListNode *cur = head;
        int n = 1;
        while (cur->next != nullptr)
        {
            cur = cur->next;
            n++;
        }
        return n;
    }
};