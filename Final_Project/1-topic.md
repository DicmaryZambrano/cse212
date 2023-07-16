# What is a Queue?

The Queue abstract data type is another fundamental data structure. It is quite similar to the stack, which is a collection of objects that can be inserted and removed following a LIFO (last-in, first-out) principle. The difference between a queue and a stack is that the queue follows a FIFO (first-in, first-out) principle, which means that the first element that is added to the queue is the first item that is processed or accessed.

A good example for a queue is a how calls are handled on a call center, when a customer calls the call center, their call is added to a queue, and the next available agent takes the first call in the queue. This ensures that customers are served in the order in which they called, with the oldest call being served first.

![Example of a call center recieving calls in a FIFO dicipline](https://i.imgur.com/vcVJt8p.jpg)

The element which will be removed first from the queue is typically called the head and the element which will be removed last from the queue is called the tails or rear.

## Types of Queues

There are many different types of queues, each with its own unique characteristics and use cases. Here are some common types of queues:

- Simple Queue: A basic queue where items are added to the back and removed from the front

- Circular Queue: A type of queue where the front and back of the queues are connected like a circle. This allows items to be added and removed from the queue in a circular fashion.

- Priority Queue: This queue will remove the items with the highest priority first and the items with the lower’s priority last, if two items have the same priority level then it will remove the item that entered the queue first. The performance depends on the implementation, a binary head-based priority queue typically has a O(log n) time complexity for both enqueue and dequeue operations.

- Deque: A double ended queue is a queue where its items can be added or removed from both the front and the back of the queue. This allows for more flexibility in how the queue is managed. It has a O(1) time complexity for enqueue and dequeue operations at both ends.

This are not the only types of queues you will find on your career but are fairly common, we will not be touching upon all the kind of queues you can make but for the purposes of this tutorial we will be working with simple queues and priority queues.

## Basic Operations on Queues

You might have already seen some of these operations mentioned on the previous section, the terms enqueue and dequeue have been mentioned multiple times to describe the action of taking out of the queue and putting an item inside of the queue. There are other kinds of operations that you can do in a queue as you can see in the table below.

| Operation | Example               | Description                                                   |
| --------- | --------------------- | ------------------------------------------------------------- |
| Enqueue   | `queue.enqueue(item)` | Adds an item to the back of the queue.                        |
| Dequeue   | `queue.dequeue()`     | Removes an item from the front of the queue and returns it.   |
| Is empty  | `queue.is_empty()`    | Returns true if the queue is empty, false otherwise.          |
| Size      | `queue.size()`        | Returns the size of the queue.                                |
| Clear     | `queue.clear()`       | Removes all items from the queue and resets its size to zero. |
| Reverse   | `queue.reverse()`     | Reverses the order of the items in the queue.                 |

These are just a few basic operations you can do with queues, there are others like Peek that return the value on the front of the queue without returning it or search that search’s for an item on the queue, but we will be keeping it simple by starting with the operations with the simplest time complexity.

## Queues in Python

Let’s see how we can implement these operations in code, similar to stack queues can also be represented with a list in python. We can dequeue and item by always removing from the index [0] that is the start of the list and we can also use append to enqueue into the list. Another function of the list that we can use it the len() that will give you the size of our list.

| Operation | Python Code                                            | Performance | Description                                                     |
| --------- | ------------------------------------------------------ | ----------- | --------------------------------------------------------------- |
| Enqueue   | `queue.append(value)`                                  | O(1)        | Adds an item to the back of the queue.                          |
| Dequeue   | `front = queue[0] return queue.pop(0)`                 | O(n)        | Removes an item from the front of the queue and returns it      |
| In empty  | `if queue.size() == 0: return true else: return false` | O(1)        | Returns true if the queue is empty, false otherwise             |
| Size      | `size = len(queue) return size`                        | O(1)        | returns the item at the front of the queue without removing it. |

By using a list for our queue some operations will have a different time complexity than others by the nature of how dynamic arrays work, note that this isn’t the only way you can implement the queue.

## Real life application for Queues

Now it is time to get our hands dirty and start typing some code, for this first example we will create a queue for a call center. The call center needs a queue because they are not able to attend the customers in a FIFO order and they feel frustrated for the inconsistent waiting times, so they hope you can help them solve this problem.

![Worried call center employee](https://i.imgur.com/RmxOuSu.jpg)

These are the requirenments:

- They have to be able to get calls out of the queue
- They have to be able to get calls into the queue
- They need to know how big the queue is
- Ensure the queue works correctly and there are no errors

Lest start by creating a simple queue object and store the queue as a python list:

```python
class Simple_Queue:
    def __init__(self):
        # Use a list to initialize the queue.
        self.queue = []
```

Now we need to implement the enqueue method

```python
def enqueue(self, value):
    # Put the value provided into the queue
    self.queue.append(value)
```

Next step is to implement the dequeue method

```python
def dequeue(self):
    # Take out and return the value in the [0] index
    value = self.queue.pop(0)
    return value
```

Good job, we have implemented the first two basic operations for the queue, but it would also be useful for the call center to know how long of a waiting list they have

Lest create the size method for our queue

```python
def size(self):
    # Return the size of the queue
    return len(self.queue)
```

Now with the size function we can easily create our is_empty function, this will be useful later

```python
def is_empty(self):
    # Return True if the queue is empty, False otherwise
    if self.size() == 0:
        return True
    else:
        return False
```

Perfect! Everything looks quite alright but if we tested this code right now and decided to dequeue an empty queue we would get an index error. Now the `is_empty()` function will come in handy, lets fix the dequeue code to handle the error.

```python
def dequeue(self):
    # Take out and return the value in the [0] index
    if self.is_empty():
        raise IndexError("Queue is empty")
    value = self.queue.pop(0)
    return value
```

This should be good enough, let look at the full code!

```python
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
```

After giving this code to the call center they noticed several problems on their service, their queues got way too long but at least they were now able to identify which call to respond first. Thanks to you they will be able to provide a better service

![Happy call center employee](https://i.imgur.com/VHwuaXx.jpg)

## Example Problem

Now it is time for you to solve the next problem, this time we will use Simple_Queue as a base for a priority queue. Here is the problem

A 2 Michelin star restaurant wants to implement a priority queue for their reservations. They want to prioritize VIP customers (priority level: 3), regular customers (priority level: 2), and walk-ins (priority level: 1) in that order. They want to be able to add new reservations to the queue, remove reservations from the queue when customers are seated, and check the size of the queue at any time.

To solve this problem, we can use the Simple_Queue structure as a basis for our priority queue. We can modify the enqueue method to take in an additional parameter, priority, which indicates the priority of the reservation. We can then modify the dequeue method to remove the highest priority reservation from the queue.

Hint: You can use tuples inside of the dynamic list like this [ customer, priority ]

Requirements:

- The Priority_Queue class should be based on the Simple_Queue class showed previously.

- The Priority_Queue class should support adding elements to the queue with an associated priority.

- The Priority_Queue class should remove elements from the queue in order of their priority, with higher priority elements being removed first.

- The Priority_Queue class should raise an IndexError if an attempt is made to remove an element from an empty queue.

Copy the code below to start working on your solution, compare your solution to [this example solution](python/01_priority_queue_solution.py).

```python
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

# Remove reservations from the queue in order of their priority
print(queue.dequeue()) # "VIP customer"
print(queue.dequeue()) # "Regular customer"
print(queue.dequeue()) # "Walk-in customer"

# Get the size of the queue
print(queue.size()) # 0

# Create more test cases if you would like
```
