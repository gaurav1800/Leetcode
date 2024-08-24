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
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        
        if (!head || !head->next || left == right) {
            return head;
        }
        
        ListNode *dummy = new ListNode(0, head);
        
        ListNode *current = dummy;
        
        
        for(int i = 0; i < left-1; i++) {
            current = current->next;
        }
        
        
        ListNode *prev = current;
        current = current->next;
        
        for(int i = left; i < right; i++) {
            ListNode *next = current->next;
            current->next = next->next;
            next->next = prev->next;
            prev->next = next;
        }
        
        return dummy->next;  
        
        
        
        
        
     
        
        
        
    }
};