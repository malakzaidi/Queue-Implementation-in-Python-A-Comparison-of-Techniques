class Queue:
    def __init__(self):
        """Initialize an empty queue."""
        self.elements = []  # List to store queue elements
        self.head = 0       # Index of the head of the queue
        self.tail = 0       # Number of elements in the queue

    def enqueue(self, x):
        """Add an element to the end of the queue."""
        if self.tail == len(self.elements):  # If the queue is full, expand it
            self.elements.append(None)  # Create a placeholder
        self.elements[self.tail] = x  # Place the new element at the tail
        self.tail += 1  # Increment the tail index

    def dequeue(self):
        """Remove and return the element at the head of the queue."""
        if self.is_empty():
            print("The queue is empty.")
            return None
        element = self.elements[self.head]  # Retrieve the head element
        self.head += 1  # Increment the head index

        # Reset the queue if it becomes empty after dequeuing
        if self.head == self.tail:
            self.head = 0
            self.tail = 0
            self.elements = []  # Reset the list
        return element

    def peek(self):
        """Return the element at the head of the queue without removing it."""
        if self.is_empty():
            print("The queue is empty.")
            return None
        return self.elements[self.head]

    def is_empty(self):
        """Check if the queue is empty."""
        return self.head == self.tail

    def clear(self):
        """Remove all elements from the queue."""
        self.elements = []
        self.head = 0
        self.tail = 0

    def count(self, x):
        """Count the occurrences of a specific element in the queue."""
        count = 0
        for i in range(self.head, self.tail):
            if self.elements[i] == x:
                count += 1
        return count

    def pop(self, index):
        """Remove and return the element at a specific index in the queue."""
        if index < 0 or index >= self.tail - self.head:
            print("Index out of range.")
            return None
        index += self.head  # Adjust index to match the internal list
        element = self.elements[index]

        # Shift elements left to fill the gap
        for i in range(index, self.tail - 1):
            self.elements[i] = self.elements[i + 1]
        self.tail -= 1  # Decrement the tail index
        return element

    def remove(self, x):
        """Remove the first occurrence of a specific element in the queue."""
        for i in range(self.head, self.tail):
            if self.elements[i] == x:
                return self.pop(i - self.head)
        print("Element not found.")
        return None

    def reverse(self):
        """Reverse the order of elements in the queue."""
        for i in range((self.tail - self.head) // 2):
            left = self.head + i
            right = self.tail - 1 - i
            self.elements[left], self.elements[right] = self.elements[right], self.elements[left]

    def sort(self):
        """Sort the elements in the queue in ascending order."""
        for i in range(self.head, self.tail):
            for j in range(i + 1, self.tail):
                if self.elements[i] > self.elements[j]:
                    self.elements[i], self.elements[j] = self.elements[j], self.elements[i]

    def copy(self):
        """Return a copy of the queue."""
        new_queue = Queue()
        new_queue.elements = self.elements[self.head:self.tail]
        new_queue.head = 0
        new_queue.tail = self.tail - self.head
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
    print("Queue after dequeuing:", queue.elements[queue.head:queue.tail])  # Output: [2, 3, 4]

    # Check if the queue is empty
    print("Is the queue empty?", queue.is_empty())  # Output: False

    # Count occurrences of an element
    print("Count of 2 in the queue:", queue.count(2))  # Output: 1

    # Reverse the queue
    queue.reverse()
    print("Queue after reversing:", queue.elements[queue.head:queue.tail])  # Output: [4, 3, 2]

    # Sort the queue
    queue.sort()
    print("Queue after sorting:", queue.elements[queue.head:queue.tail])  # Output: [2, 3, 4]

    # Clear the queue
    queue.clear()
    print("Queue after clearing:", queue.elements)  # Output: []

    # Copy the queue (after adding elements back)
    queue.enqueue(5)
    queue.enqueue(6)
    copied_queue = queue.copy()
    print("Copied queue elements:", copied_queue.elements)  # Output: [5, 6]

     

     