class Sentinel:
    def __init__(self, prev, next):
        self.prev = prev
        self.next = next
    def __len__(self):
        return 0
    def __getitem__(self, i):
        raise IndexError("Index out of bounds")
    def __str__(self):
        return ""
    def __repr__(self):
        return "Sentinel()"

class LinkedList:
    def __init__(self, item, prev, next):
        assert type(next) == LinkedList or type(next) == Sentinel, "Next must be a LinkedList"
        assert type(prev) == LinkedList or type(prev) == Sentinel, "Prev must be a LinkedList"
        self.item = item
        self.prev = prev
        self.next = next

    # Sequence protocol
    def __len__(self):
        return 1 + len(self.next)
    def __getitem__(self, i):
        if i == 0:
            return self.item
        return self.next[i - 1]

    # String representation protocol
    def __repr__(self):
        return "LinkedList(" + repr(self.item) + ", "  + repr(self.next) + ")"
    def __str__(self):
        return str(self.item) + "-> " + str(self.next)

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
            print(new_node)
            if not linked_lst.next:
                linked_lst.next = new_node
            else:
                linked_lst.prev.next = new_node
            linked_lst.prev = new_node
        return linked_lst if not linked_lst.next else linked_lst.next




