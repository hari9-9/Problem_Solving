SinglyLinkedListNode* insertNodeAtPosition(SinglyLinkedListNode* head, int data, int position) {
    SinglyLinkedListNode * newNode = new SinglyLinkedListNode(data);
    int count=1;
    for(SinglyLinkedListNode * temp = head; temp!=NULL; temp=temp->next)
    {
        if(count==position)
        {
            newNode->next = temp->next;
            temp->next=newNode;
            break;
        }
        count++;
    }
    return head;
}
