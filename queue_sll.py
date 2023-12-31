# Name: Shuyao Zeng
# OSU Email: zengs@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 3
# Due Date: 07/24/2023
# Description: Implement a Queue ADT class which includes enqueue(), dequeue() and front() methods.


from SLNode import SLNode


class QueueException(Exception):
    """
    Custom exception to be used by Queue class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Queue:
    def __init__(self):
        """
        Initialize new queue with head and tail nodes
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = None
        self._tail = None

    def __str__(self):
        """
        Return content of queue in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'QUEUE ['
        if not self.is_empty():
            node = self._head
            out = out + str(node.value)
            node = node.next
            while node:
                out = out + ' -> ' + str(node.value)
                node = node.next
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the queue is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._head is None

    def size(self) -> int:
        """
        Return number of elements currently in the queue
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        node = self._head
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    # -----------------------------------------------------------------------

    def enqueue(self, value: object) -> None:
        """
        Add a new value to the end of the queue.
        """
        node = SLNode(value)
        if self.is_empty() is True:
            self._head = node
            self._tail = node
        else:
            self._tail.next = node
            self._tail = node

    def dequeue(self) -> object:
        """
        Remove and return the value from the beginning of the queue. Raise a custom "QueueException"
        if the queue is empty.
        """
        if self.is_empty() is True:
            raise QueueException
        else:
            value_to_remove = self._head.value
            self._head = self._head.next
            return value_to_remove

    def front(self) -> object:
        """
        Return the value of the front element of the queue without removing it. Raise a custom
        "QueueException" if the queue is empty.
        """
        if self.is_empty() is True:
            raise QueueException
        return self._head.value


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# enqueue example 1")
    q = Queue()
    print(q)
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)

    print("\n# dequeue example 1")
    q = Queue()
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)
    for i in range(6):
        try:
            print(q.dequeue())
        except Exception as e:
            print("No elements in queue", type(e))

    print('\n#front example 1')
    q = Queue()
    print(q)
    for value in ['A', 'B', 'C', 'D']:
        try:
            print(q.front())
        except Exception as e:
            print("No elements in queue", type(e))
        q.enqueue(value)
    print(q)
