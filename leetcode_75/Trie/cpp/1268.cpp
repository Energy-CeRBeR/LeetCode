#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class TrieNode
{
public:
    vector<TrieNode *> children;
    vector<string> words;

    TrieNode()
    {
        children.resize(26, nullptr);
    }
};

class Trie
{

    TrieNode *root;
    TrieNode *node;

public:
    Trie()
    {
        root = new TrieNode();
        node = root;
    }

    void insert(string word)
    {
        TrieNode *node = root;
        for (char c : word)
        {
            int ind = c - 'a';
            if (!node->children[ind])
                node->children[ind] = new TrieNode();
            node = node->children[ind];

            if (node->words.size() < 3)
                node->words.push_back(word);
        }
    }

    vector<string> find_word_by_prefix(char c)
    {
        if (this->node && this->node->children[(int)(c - 'a')])
        {
            this->node = this->node->children[(int)(c - 'a')];
            return this->node->words;
        }
        else
        {
            this->node = nullptr;
            return {};
        }
    }
};

class Solution
{
public:
    vector<vector<string>> suggestedProducts(vector<string> &products, string searchWord)
    {
        Trie trie = Trie();
        sort(products.begin(), products.end());

        for (string product : products)
        {
            trie.insert(product);
        }

        vector<vector<string>> result;
        for (char c : searchWord)
        {
            result.push_back(trie.find_word_by_prefix(c));
        }

        return result;
    }
};