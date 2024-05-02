/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        
        int i = 0;
        
        ListNode* current = head;
        
        while (current != NULL) {
            i++;
            current = current->next;
        }
        
        if (i == n) {
            return head->next;
        }
        
        current = head;
        
        while (i != n+1) {
            current = current->next;
            i--;
        }
        
        current->next = current->next->next;
        
        return head;
        
        
        
        
    }
};