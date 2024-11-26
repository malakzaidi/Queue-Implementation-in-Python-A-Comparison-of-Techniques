class Queue:
    def __init__(self):
        """Initialize an empty queue."""
        self.elements = []  # List to store queue elements

    def enqueue(self, x):
        """Add an element to the end of the queue."""
        self.elements.append(x)

    def dequeue(self):
        """Remove and return the element at the head of the queue."""
        if self.is_empty():
            print("The queue is empty.")
            return None
        return self.elements.pop(0)

    def peek(self):
        """Return the element at the head of the queue without removing it."""
        if self.is_empty():
            print("The queue is empty.")
            return None
        return self.elements[0]

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.elements) == 0

    def clear(self):
        """Remove all elements from the queue."""
        self.elements.clear()

    def count(self, x):
        """Count the occurrences of a specific element in the queue."""
        return self.elements.count(x)

    def pop(self, index):
        """Remove and return the element at a specific index in the queue."""
        if index < 0 or index >= len(self.elements):
            print("Index out of range.")
            return None
        return self.elements.pop(index)

    def remove(self, x):
        """Remove the first occurrence of a specific element in the queue."""
        try:
            self.elements.remove(x)
        except ValueError:
            print("Element not found.")

    def reverse(self):
        """Reverse the order of elements in the queue."""
        self.elements.reverse()

    def sort(self):
        """Sort the elements in the queue in ascending order."""
        self.elements.sort()

    def copy(self):
        """Return a copy of the queue."""
        new_queue = Queue()
        new_queue.elements = self.elements.copy()
        return new_queue


# Example Usage
if __name__ == "__main__":
    queue = Queue()

    # Adding elements to the queue
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    print("Queue elements:", queue.elements)  # Output: [1, 2, 3, 4]

    # Peek at the head of the queue
    print("Head of the queue:", queue.peek())  # Output: 1

    # Dequeue elements
    print("Dequeued element:", queue.dequeue())  # Output: 1
    print("Queue after dequeuing:", queue.elements)  # Output: [2, 3, 4]

    # Check if the queue is empty
    print("Is the queue empty?", queue.is_empty())  # Output: False

    # Count occurrences of an element
    print("Count of 2 in the queue:", queue.count(2))  # Output: 1

    # Reverse the queue
    queue.reverse()
    print("Queue after reversing:", queue.elements)  # Output: [4, 3, 2]

    # Sort the queue
    queue.sort()
    print("Queue after sorting:", queue.elements)  # Output: [2, 3, 4]

    # Clear the queue
    queue.clear()
    print("Queue after clearing:", queue.elements)  # Output: []

    # Copy the queue (after adding elements back)
    queue.enqueue(5)
    queue.enqueue(6)
    copied_queue = queue.copy()
    print("Copied queue elements:", copied_queue.elements)  # Output: [5, 6]
