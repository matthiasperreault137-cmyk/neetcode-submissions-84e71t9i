/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode last = head;
        if(last == null){
            return null;
        }
        ListNode cur = head.next;
        if(cur == null){
            return head;
        }
        last.next = null;
        while (cur != null){
            ListNode temp = cur.next;
            cur.next = last;
            last = cur;
            cur = temp;
        }
        return last;
    }
}
