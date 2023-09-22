/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public ListNode MergeTwoLists(ListNode list1, ListNode list2) {
        ListNode retNode = new ListNode();
        ListNode tempNode = retNode;

        while(list1 !=null && list2 != null){
            ListNode newNode = new ListNode();
               if(list1.val < list2.val) {
                    newNode.val = list1.val;
                    tempNode.next = newNode;
                    tempNode = newNode;
                    list1 = list1.next;
                } else {
                    newNode.val = list2.val;
                    tempNode.next = newNode;
                    tempNode = newNode;
                    list2 = list2.next; 
                } 
        }
        
        while(list1 !=null){
            ListNode newNode = new ListNode();
            newNode.val = list1.val;
            tempNode.next = newNode;
            tempNode = newNode;
            list1 = list1.next;
        }
        
        while(list2 !=null){
            ListNode newNode = new ListNode();
            newNode.val = list2.val;
            tempNode.next = newNode;
            tempNode = newNode;
            list2 = list2.next;
        }
        
        return retNode.next;
    }
}