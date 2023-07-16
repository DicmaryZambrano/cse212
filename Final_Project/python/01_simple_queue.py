'''
The call center needs a queue because they are not able to attend the customers in a FIFO 
order and they feel frustrated for the inconsistent waiting times, so they hope you can help 
them solve this problem.
'''


class Simple_Queue:
    def __init__(self):
        # Use a list to initialize the queue. 
        self.queue = []

    def enqueue(self, value):
        # Put the value provided into the queue
        self.queue.append(value)

    def dequeue(self):
        # Take out and return the value in the [0] index
        if self.is_empty():
            raise IndexError("Queue is empty")
        value = self.queue.pop(0)
        return value

    def size(self):
        # Return the size of the queue
        return len(self.queue)

    def is_empty(self):
        # Return True if the queue is empty, False otherwise
        if self.size() == 0:
            return True
        else:
            return False

# Create a new queue object
queue = Simple_Queue()

# Test enqueue method
queue.enqueue('caller #1234')
queue.enqueue('caller #4123')
queue.enqueue('caller #3231')

assert queue.size() == 3

# Test dequeue method
assert queue.dequeue() == 'caller #1234'
assert queue.size() == 2

# Test is_empty method
assert queue.is_empty() == False

# Test dequeue on empty queue
empty_queue = Simple_Queue()

try:
    empty_queue.dequeue()
except IndexError:
    print("Successfully raised IndexError for dequeue on empty queue")
else:
    raise AssertionError("Failed to raise IndexError for dequeue on empty queue")