bool has_cycle(Node* head) {
    if (head==NULL) return false;
    Node * temp2=head;
    int count=1;
    for(Node * temp = head->next; temp!=NULL; temp=temp->next)
    {
        if(count%2==0) temp2=temp2->next;
        if(temp==temp2) return true;
        count++;
    }
    return false;
}
