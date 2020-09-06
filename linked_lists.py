
class LinkedListNode:
    """Node in linked list"""
    def __init__(self, value):
        """create a node"""
        self.next = None
        self.prev = None
        self.value = value


class LinkedList:
    """LL abstraction"""
    def __init__(self, data: (float,) = ()):

        self.head = None
        prev = None
        for value in data:
            n = LinkedListNode(value)
            if prev is None:
                self.head = n
            else:
                prev.next = n
            prev = n

        self.tail = prev

    def traverse(self) -> None:
        """Move across nodes"""
        cursor = self.head
        while cursor is not None:
            print(cursor.value)
            cursor = cursor.next

    def deduplicate(self):
        """Remove duplicates"""
        cursor, last, exists = self.head, None, set()
        while cursor is not None:
            if last is not None and cursor.value in exists:
                last.next = cursor.next.next if cursor.next is not None else None
            else:
                exists |= {cursor.value}
            last, cursor = cursor, cursor.next
        return last

    def k_from_head(self, k: int) -> None or LinkedListNode:
        """Get selected"""
        cursor = self.head
        while cursor.next is not None and k:
            cursor = cursor.next
            k -= 1
        return cursor.value

    def k_from_end(self, k: int) -> None or LinkedListNode:
        cursor = self.head
        total = -k
        while cursor is not None:
            cursor = cursor.next
            total += 1

        assert total > 0

        cursor = self.head
        while cursor is not None and total:
            cursor.next = cursor.next
            total -= 1
        return cursor.value

    def prepend(self, value: float) -> None:
        n = LinkedListNode(value)
        n.next, self.head = self.head, n

    def append(self, value: float) -> None:
        n = LinkedListNode(value)
        if self.head is None:
            self.head = n
        if self.tail is not None:
            self.tail.next = n
        self.tail = n

    def add(self, other):
        ...


class DoublyLinkedList(LinkedList):
    prev = None  # only for doubly-linked

    def __init__(self, data: (float,) = ()):
        LinkedList.__init__(self, data)
        cursor = self.head
        while cursor.next is not None:
            cursor.next.prev = cursor

    def k_from_end(self, n: int = None) -> None or LinkedListNode:

        _next = self.tail
        _last = None
        while _next is not None and (n is None or n):
            _last = _next
            _next = _next.prev
            if n:
                n -= 1
        return _last

    def traverse_backward(self) -> None:
        cursor = self.tail
        while cursor is not None:
            print(cursor.value)
            cursor = cursor.prev

    def push_front(self, value: float) -> None:
        n = LinkedListNode(value)
        n.next = self.head
        self.head.prev = n
        self.head = n

    def push_back(self, value: float) -> None:
        n = LinkedListNode(value)
        n.prev = self.tail
        if self.head is None:
            self.head = n
        if self.tail is not None:
            self.tail.next = n
        self.tail = n

    def insert_after(self, insert: LinkedListNode, ref: LinkedListNode):
        ...

    def insert_before(self, insert: LinkedListNode, ref: LinkedListNode):
        ...
