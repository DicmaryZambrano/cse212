'''
A 2 Michelin star restaurant wants to implement a priority queue for their reservations. 
They want to prioritize VIP customers, regular customers, and walk-ins in that order. 
They want to be able to add new reservations to the queue, remove reservations from the queue 
when customers are seated, and check the size of the queue at any time.
'''

class Priority_Queue:
    def __init__(self):
        # Use a list to initialize the queue
        self.queue = []

    def enqueue(self, value, priority):
        # Put the value and its priority into the queue as a tuple
        pass

    def _get_highest_priority_item(self):
        # Find and return the item with the highest priority
        pass

    def dequeue(self):
        # Remove and return the item with the highest priority
        highest_priority_item = self._get_highest_priority_item()
        self.queue.remove(highest_priority_item)
        return highest_priority_item[0]

    def size(self):
        # Return the size of the queue
        return len(self.queue)

    def is_empty(self):
        # Return True if the queue is empty, False otherwise
        return self.size() == 0

# Create a new priority queue object
queue = Priority_Queue()

# Add new reservations to the queue with their priorities
queue.enqueue("VIP customer", 3)
queue.enqueue("Regular customer", 2)
queue.enqueue("Walk-in customer", 1)
print("\n======================")
# Remove reservations from the queue in order of their priority
print(queue.dequeue()) # "VIP customer"
print(queue.dequeue()) # "Regular customer"
print(queue.dequeue()) # "Walk-in customer"
print("\n======================")
# Get the size of the queue
print(f"size: {queue.size()}") # 0
print("\n======================")