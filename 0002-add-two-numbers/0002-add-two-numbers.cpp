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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        
        ListNode* curr1 = l1;
        ListNode* curr2 = l2;
        
        ListNode* head = new ListNode(0);
        ListNode* currh = head;
        
        int carry = 0;
        
        
        while (curr1 != NULL || curr2 != NULL || carry != 0) {
            int sum = carry;
            
            if (curr1 != NULL) {
                sum += curr1->val;
                curr1 = curr1->next;
            }
            if (curr2 != NULL) {
                sum += curr2->val;
                curr2 = curr2->next;
            }
            
            carry = sum/10;
            sum %= 10;
            
            currh->next = new ListNode(sum);
            currh = currh->next;
        }
        
        return head->next;
        
    }
};