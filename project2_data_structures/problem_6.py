class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1, llist_2):
    list_union = LinkedList()
    union_repeat = []

    head1 = llist_1.head
    if head1 is None and llist_2.head is not None:
        return llist_2
    if llist_2.head is None and head1 is not None:
        return llist_1
    while head1:
        head2 = llist_2.head
        while head2:
            if head1.value != head2.value and head1.value not in union_repeat:
                list_union.append(head1)
                union_repeat.append(head1.value)
            if head2.value not in union_repeat:
                list_union.append(head2)
                union_repeat.append(head2.value)
            head2 = head2.next
        head1 = head1.next

    return list_union


def intersection(llist_1, llist_2):
    intersect = LinkedList()
    intersection_repeat = []

    head1 = llist_1.head
    while head1:
        head2 = llist_2.head
        while head2:
            if head1.value == head2.value and head1.value not in intersection_repeat:
                intersect.append(head1)
                intersection_repeat.append(head1.value)
            head2 = head2.next
        head1 = head1.next

    if intersect.head is None:
        return 'There is no intersection'
    return intersect


### TEST CASE

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(union(linked_list_1, linked_list_2))
# 3 -> 6 -> 32 -> 4 -> 9 -> 1 -> 11 -> 21 -> 2 -> 35 -> 65 ->

print(intersection(linked_list_1, linked_list_2))
# 4 -> 6 -> 21 ->

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(union(linked_list_3, linked_list_4))
# 3 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 2 -> 4 -> 35 -> 6 -> 65 -> 23 ->

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [1, 2, 3, 4]

for i in element_1:
    linked_list_5.append(i)

print(union(linked_list_5, linked_list_6))
# 1 -> 2 -> 3 -> 4 ->
print(intersection(linked_list_5, linked_list_6))
# There is no intersection
