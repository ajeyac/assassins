class ListNode:
    def __init__(self, item, prev, next):
        self.item = item
        self.prev = prev
        self.next = next

    def __repr__(self):
        return repr(self.item)

class LinkedList:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail

    # Sequence protocol
    def __len__(self):
        if not head:
            return 0
        curr, total = self.head, 1
        while curr is not self.tail:
            total += 1
            curr = curr.next
        return total

    def __getitem__(self, i):
        curr = self.head
        while curr:
            if i == 0:
                return curr
            curr, i = curr.next, i - 1
        raise IndexError("Index out of range")

    # String representation protocol
    def __repr__(self):
        if not self.head:
            return ''

    def __str__(self):
        string = ''
        for el in self:
            string += "-> " + el
        return string

    # Equality testing
    def __eq__(self, other):
        assert type(other) == LinkedList, "Cannot compare LinkedList and " + str(type(other))
        return self.item == other.item and self.next == other.next

    # Remove obj (takes in a pointer to item)
    def remove(self, obj):
        if self.item is obj:
            self.prev.next = self.next
            self.next.prev = self.prev
            self.item, self.next, self.prev = None, None, None

    def create(lst):
        linked_lst = Sentinel(None, None)
        for elem in lst:
            new_node = LinkedList(elem, linked_lst.prev, linked_lst)
            if not linked_lst.next:
                linked_lst.next = new_node
            else:
                linked_lst.prev.next = new_node
            linked_lst.prev = new_node
        return linked_lst if not linked_lst.next else linked_lst.next




