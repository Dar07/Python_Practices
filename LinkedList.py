#A node Class 
class node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

#A linked_list Class
class linked_list:
    def __init__(self):
        self.head = None

    #Method to add an elements at the beginning of the list
    def add_at_front(self, data):
        self.head = node(data=data, next=self.head)

    #Method to check if list is Empty
    def is_empty(self):
        return self.head == None

    #Method to add elements to the end of the list
    def add_at_end(self, data):
        if not self.head:
            self.head = node(data=data)
            return
        curr=self.head
        while curr.next:
            curr = curr.next
        curr.next = node(data=data)

    #Method to delete nodes
    def delete_node(self, key):
        curr = self.head
        prev = None
        while curr and curr.data != key:
            prev=curr
            curr=curr.next
        if prev is None:
            self.head = curr.next
        elif curr:
            prev.next = curr.next
            curr.next = None

    #Method to get the last node
    def get_last_node(self):
        temp=self.head
        while(temp.next is not None):
            temp=temp.next
        return temp.data

    #Method to print the list
    def print_list(self):
        node=self.head
        while node != None:
            print(node.data, end =" => ")
            node =node.next

s = linked_list() 
s.add_at_front(5)
s.add_at_end(8)
s.add_at_front(9)

s.print_list()
