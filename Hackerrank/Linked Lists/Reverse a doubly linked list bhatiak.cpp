//GFG solution.
DoublyLinkedListNode* reverse(DoublyLinkedListNode* head) {
    DoublyLinkedListNode * temp = NULL;
    DoublyLinkedListNode * cur = head;

    while(cur!=NULL)
    {
        temp=cur->prev;
        cur->prev=cur->next;
        cur->next=temp;
        cur=cur->prev;
    }
    if(temp!=NULL)
        head=temp->prev;
    return head;
}
