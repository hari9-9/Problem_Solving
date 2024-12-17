public class ListNodeIterator {

    // write your code here
    ListNode head;
    ListNode curr;

    ListNodeIterator(ListNode node) {
        // write your code here
        head = node;
        curr = new ListNode(-1);
        curr.next = head;
    }

    boolean hasNext() {
        // write your code here
        return curr.next !=null;
    }

    ListNode next() {
        return hasNext() ? (curr = curr.next) : null;
        // write your code here
    }

}

// public class ListNode {
//     public int val;
//     public ListNode next;

//     public ListNode(int val) {
//         this.val = val;
//         this.next = null;
//     }

//     public ListNodeIterator getIterator() {
//         return new ListNodeIterator(this);
//     }

//     @Override
//     public String toString() {
//         return "" + this.val;
//     }
// }

// public class Main {
//     public static void main(String[] args) {
//         ListNode node1 = new ListNode(10);
//         ListNode node2 = new ListNode(20);
//         ListNode node3 = new ListNode(30);
//         node1.next = node2;
//         node2.next = node3;
//         ListNodeIterator iterator = node1.getIterator();
//         while (iterator.hasNext()) {
//             System.out.println(iterator.next());
//         }
//     }
// }
