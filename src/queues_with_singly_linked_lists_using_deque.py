class Node:
    def __init__(self, data):
        """Initialize a node with data and a reference to the next node."""
        self.data = data
        self.next = None


class LinkedListQueue:
    def __init__(self):
        """Initialize an empty linked list-based queue."""
        self.head = None  # Points to the first node
        self.tail = None  # Points to the last node
        self.size = 0     # Tracks the size of the queue

    def enqueue(self, data):
        """Add an element to the end of the queue."""
        new_node = Node(data)
        if self.head is None:
            # If the queue is empty, both head and tail point to the new node
            self.head = self.tail = new_node
        else:
            # Add the new node to the end and update the tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def dequeue(self):
        """Remove and return the element at the front of the queue."""
        if self.is_empty():
            print("The queue is empty.")
            return None
        data = self.head.data  # Retrieve data from the head node
        self.head = self.head.next  # Move the head pointer to the next node
        if self.head is None:
            # If the queue is now empty, reset the tail
            self.tail = None
        self.size -= 1
        return data

    def peek(self):
        """Return the element at the front of the queue without removing it."""
        if self.is_empty():
            print("The queue is empty.")
            return None
        return self.head.data

    def is_empty(self):
        """Check if the queue is empty."""
        return self.head is None

    def clear(self):
        """Remove all elements from the queue."""
        self.head = None
        self.tail = None
        self.size = 0

    def count(self, data):
        """Count the occurrences of a specific element in the queue."""
        count = 0
        current = self.head
        while current:
            if current.data == data:
                count += 1
            current = current.next
        return count

    def remove(self, data):
        """Remove the first occurrence of a specific element in the queue."""
        if self.is_empty():
            print("The queue is empty.")
            return None

        # Special case: removing the head
        if self.head.data == data:
            return self.dequeue()

        # Traverse the queue to find the node
        current = self.head
        while current.next and current.next.data != data:
            current = current.next

        if current.next is None:
            print("Element not found.")
            return None

        # Remove the node by skipping it
        removed_data = current.next.data
        current.next = current.next.next

        # If the removed node was the tail, update the tail
        if current.next is None:
            self.tail = current

        self.size -= 1
        return removed_data

    def reverse(self):
        """Reverse the order of elements in the queue."""
        prev = None
        current = self.head
        self.tail = self.head  # Update the tail to the old head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev  # Update the head to the old tail

    def copy(self):
        """Return a new queue that is a copy of the current queue."""
        new_queue = LinkedListQueue()
        current = self.head
        while current:
            new_queue.enqueue(current.data)
            current = current.next
        return new_queue

    def sort(self):
        """Sort the elements in the queue in ascending order."""
        # Convert linked list to list for easier sorting
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next

        elements.sort()

        # Rebuild the queue with sorted elements
        self.clear()
        for data in elements:
            self.enqueue(data)


# Example Usage
if __name__ == "__main__":
    queue = LinkedListQueue()

    # Adding elements to the queue
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(15)
    queue.enqueue(25)
    print("Queue elements after enqueueing:")
    current = queue.head
    while current:
        print(current.data, end=" ")
        current = current.next
    print("\n")

    # Peek at the front of the queue
    print("Peek at the front:", queue.peek())  # Output: 10

    # Dequeue elements
    print("Dequeued:", queue.dequeue())  # Output: 10
    print("Queue after dequeuing:")
    current = queue.head
    while current:
        print(current.data, end=" ")
        current = current.next
    print("\n")

    # Reverse the queue
    queue.reverse()
    print("Queue after reversing:")
    current = queue.head
    while current:
        print(current.data, end=" ")
        current = current.next
    print("\n")

    # Sort the queue
    queue.sort()
    print("Queue after sorting:")
    current = queue.head
    while current:
        print(current.data, end=" ")
        current = current.next
    print("\n")

    # Count occurrences of a value
    print("Count of 20 in the queue:", queue.count(20))

    # Clear the queue
    queue.clear()
    print("Queue after clearing:", "Empty" if queue.is_empty() else "Not empty")
