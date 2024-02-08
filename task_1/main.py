class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = Node(data)

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def search_element(self, data) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def _sorted_merge(self, a, b):
        result = None

        if a is None:
            return b
        if b is None:
            return a

        if a.data <= b.data:
            result = a
            result.next = self._sorted_merge(a.next, b)
        else:
            result = b
            result.next = self._sorted_merge(a, b.next)

        return result

    def _front_back_split(self, source):
        if source is None or source.next is None:
            return source, None

        slow = source
        fast = source.next

        while fast is not None:
            fast = fast.next
            if fast is not None:
                fast = fast.next
                slow = slow.next

        front = source
        back = slow.next
        slow.next = None

        return front, back

    def _merge_sort(self, head):
        if head is None or head.next is None:
            return head

        front, back = self._front_back_split(head)

        front = self._merge_sort(front)
        back = self._merge_sort(back)

        return self._sorted_merge(front, back)

    def sort(self):
        self.head = self._merge_sort(self.head)


def merge_sorted_lists(list1, list2):
    merged_list = LinkedList()

    while list1.head is not None or list2.head is not None:
        if list1.head and list2.head:
            if list1.head.data < list2.head.data:
                merged_list.insert_at_end(list1.head.data)
                list1.head = list1.head.next
            else:
                merged_list.insert_at_end(list2.head.data)
                list2.head = list2.head.next
        elif list1.head:
            merged_list.insert_at_end(list1.head.data)
            list1.head = list1.head.next
        elif list2.head:
            merged_list.insert_at_end(list2.head.data)
            list2.head = list2.head.next

    return merged_list


if __name__ == '__main__':
    llist = LinkedList()

    llist.insert_at_beginning(5)
    llist.insert_at_beginning(10)
    llist.insert_at_beginning(15)

    llist.insert_at_end(20)
    llist.insert_at_end(25)

    print("Linked list:")
    llist.print_list()

    llist.reverse()

    print("Linked list after reversing:")
    llist.print_list()

    llist.sort()

    print("Linked list after sorting:")
    llist.print_list()

    llist_2 = LinkedList()

    llist_2.insert_at_end(11)
    llist_2.insert_at_end(35)
    llist_2.insert_at_end(40)

    print("Linked list 2:")
    llist_2.print_list()

    print("Linked list after merging:")
    llist_3 = merge_sorted_lists(llist, llist_2)

    llist_3.print_list()




