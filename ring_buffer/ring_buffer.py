from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # checking if there's space to add item to tail
        if self.storage.length < self.capacity:
            # adding it if there is
            self.storage.add_to_tail(item)
        else:

            # if capacity is full or the end of the list is met
            if self.current is None or self.current.next is None:
                # set current = to start of list, or head
                self.current = self.storage.head
            else:
                # increment current to next value
                # print(self.current.value)
                self.current = self.current.next
            # current value = to argument being passed in
            self.current.value = item

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        current_node = self.storage.head
        # print(current_node.value)
        while current_node is not None:
            list_buffer_contents.append(current_node.value)
            current_node = current_node.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
