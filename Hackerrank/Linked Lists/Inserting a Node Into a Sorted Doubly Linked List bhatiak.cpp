DoublyLinkedListNode* sortedInsert(DoublyLinkedListNode* head, int data) {
    DoublyLinkedListNode * newNode = new DoublyLinkedListNode(data);

    if (head==NULL)
        return newNode;

    if(head->next==NULL || head->data > data)
    {
        if (data >= head->data)
        {
            head->next=newNode;
        }
        else
        {
            newNode->next=head;
            head=newNode;
        }
        return head;
    }
    
    DoublyLinkedListNode * temp = head;
    for(; temp->next!=NULL; temp=temp->next)
    {
        if(temp->next->data > data)
        {
            newNode->next=temp->next;
            temp->next->prev = newNode;

            newNode->prev = temp;
            temp->next = newNode;
            break;
        }
    }
    if(temp->next==NULL)
    {
        temp->next=newNode;
        newNode->prev = temp;
    }
    return head;
}
