#include <string>
#include <vector>

using namespace std;

class TrieNode
{
public:
    vector<TrieNode *> child;
    bool is_word;

    TrieNode()
    {
        is_word = false;
        child.resize(26, nullptr);
    }
};

class Trie
{

    TrieNode *root;

public:
    Trie()
    {
        root = new TrieNode();
    }

    void insert(string word)
    {
        TrieNode *cur_node = this->root;
        for (auto c : word)
        {
            int ind = c - 'a';
            if (!cur_node->child[ind])
                cur_node->child[ind] = new TrieNode();
            cur_node = cur_node->child[ind];
        }
        cur_node->is_word = true;
    }

    bool search(string word)
    {
        TrieNode *cur_node = this->root;
        for (auto c : word)
        {
            int ind = c - 'a';
            if (!cur_node->child[ind])
                return false;
            cur_node = cur_node->child[ind];
        }

        return cur_node->is_word;
    }

    bool startsWith(string prefix)
    {
        TrieNode *cur_node = this->root;
        for (auto c : prefix)
        {
            int ind = c - 'a';
            if (!cur_node->child[ind])
                return false;
            cur_node = cur_node->child[ind];
        }

        return true;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */