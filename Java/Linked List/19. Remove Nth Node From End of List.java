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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        
        ListNode dummy = new ListNode();
        ListNode cur = dummy;
        cur.next = head;

        ListNode first = cur;
        ListNode sec = cur;

        while(n>0){
            sec = sec.next;
            n--;
        }

        while(sec.next != null){
            sec = sec.next;
            first = first.next;
        }

        first.next = first.next.next;

        return dummy.next;       

    }
}