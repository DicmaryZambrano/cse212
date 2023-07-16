"""
CSE212 
(c) BYU-Idaho
04-Prove - Problem 2

It is a violation of BYU-Idaho Honor Code to post or share this code with others or 
to post it online.  Storage into a personal and private repository (e.g. private
GitHub repository, unshared Google Drive folder) is acceptable.
"""

class Priority_Queue:
    """
    This queue follows the same FIFO process except that higher priority
    nodes will be dequeued before lower priority nodes.  Nodes of the same
    priority will follow the same FIFO process.
    """

    class Node:
        """
        Each node is the queue will have both a value and a priority.
        """

        def __init__(self, value, priority):
            """
            Initialize a new node
            """
            self.value = value
            self.priority = priority

        def __str__(self):
            """
            Display a single node
            """
            return "{} (Pri:{})".format(self.value, self.priority)

    def __init__(self):
        """ 
        Initialize an empty priority queue
        """
        self.queue = []

    def enqueue(self, value, priority):
        """
        Add a new value to the queue with an associated priority.  The
        node is always added to the back of the queue irregardless of 
        the priority.
        """
        new_node = Priority_Queue.Node(priority, value)
        self.queue.append(new_node)

    def dequeue(self):
        """
        Remove the next value from the queue based on the priority.  The 
        highest priority item will be removed.  In the case of multiple
        values with the same high priority, the one closest to the front
        (in traditional FIFO order) will be removed.  Priority values are
        interpreted as higher numbers have higher priority.  For example, 
        10 is a higher priority than 5.
        """

        if len(self.queue) == 0:  # Verify the queue is not empty
            print("The queue is empty.")
            return None
        # Find the index of the item with the highest priority to remove
        high_pri_index = 0
        for index in range(1, len(self.queue)):
            if self.queue[index].priority > self.queue[high_pri_index].priority:
                high_pri_index = index

            elif self.queue[index].priority == self.queue[high_pri_index].priority:
                high_pri_index = 0 
        # Remove and return the item with the highest priority
        value = self.queue[high_pri_index].value
        del self.queue[high_pri_index]
        return value
        
    def __len__(self):
        """
        Support the len() function
        """
        return len(self.queue)

    def __str__(self):
        """ 
        Suppport the str() function to provide a string representation of the
        priority queue.  This is useful for debugging.  If you have a 
        Priority_Queue object called pq, then you run print(pq) to see the 
        contents.
        """
        result = "["
        for node in self.queue:
            result += str(node)  # This uses the __str__ from the Node class
            result += ", "
        result += "]"
        return result

# Test Cases

# Test 1
# Scenario: Create a queue with the following nodes and priority: first(3) second(2) third(1)
#           dequeue by priority and print the value until the queue is empty
# Expected Result: first, second, third
print("Test 1")
nodes = Priority_Queue()
nodes.enqueue(3, "first")
nodes.enqueue(2, "second")
nodes.enqueue(1, "third")

#print(nodes) #checking to see if the queue is appending properly

node1 = nodes.dequeue()
print(node1)
node2 = nodes.dequeue()
print(node2)
node3 = nodes.dequeue()
print(node3)

# Defect(s) Found: dequeue is not deleting the node afther finding the highest priority value,
# afther storing this value the node should be removed so its not stuck on the first high priority value

print("=================")

# Test 2
# Scenario: there is more than one node with the same priority value first (3) second (2) third (2) fourth (2) 
# Expected Result: the item closest to the front of the queue will be removed and its value returned
# first, second, third, fourth

print("Test 2")
nodes = Priority_Queue()
nodes.enqueue(3, "first")
nodes.enqueue(2, "second")
nodes.enqueue(2, "third")
nodes.enqueue(2, "fourth")

#print(nodes) #checking to see if the queue is appending properly

node1 = nodes.dequeue()
print(node1)
node2 = nodes.dequeue()
print(node2)
node3 = nodes.dequeue()
print(node3)
node4 = nodes.dequeue()
print(node4)

print("=================")


# Test 3

# Scenario: a queue of nodes unorganized and with nodes with the same priority value
# Expected Result: node5 node2 node4 node1 node3

print("Test 3")
nodes = Priority_Queue()

nodes.enqueue(1, "node1")
nodes.enqueue(3, "node2")
nodes.enqueue(1, "node3")
nodes.enqueue(2, "node4")
nodes.enqueue(5, "node5")

#print(nodes) #checking to see if the queue is appending properly

node1 = nodes.dequeue()
print(node1)
node2 = nodes.dequeue()
print(node2)
node3 = nodes.dequeue()
print(node3)
node4 = nodes.dequeue()
print(node4)
node5 = nodes.dequeue()
print(node5)


# Defect(s) Found: no defects found

print("=================")

# Test 4

# Scenario: a new node is added to the queue afther dequeueing
# Expected Result: node5 node2 node4 node1 node3

print("Test 4")
nodes = Priority_Queue()

nodes.enqueue(1, "node1")
nodes.enqueue(3, "node2")
nodes.enqueue(1, "node3")
nodes.enqueue(5, "node5")

#print(nodes) #checking to see if the queue is appending properly

node1 = nodes.dequeue()
print(node1)

node2 = nodes.dequeue()

print(node2)

nodes.enqueue(2, "node4")

node3 = nodes.dequeue()

print(node3)

node4 = nodes.dequeue()

print(node4)

node5 = nodes.dequeue()
print(node5)


# Defect(s) Found: no defects found

print("=================")

# Test 4

# Scenario: there are no nodes in the list
# Expected Result: The queue is empty.

print("Test 5")
nodes = Priority_Queue()

#print(nodes) #checking to see if the queue is empthy

nodes.dequeue()


# Defect(s) Found: no defects found

print("=================")

# Overrall the code only had some small details to change, i fixed the dequeuing not deleting the
# nodes afther displaying the value, i fixed the dequeing 
# not working propperly when a value has the same priority as other values by adding a check to see
# if the priority is the same on more than one value, making them follow the FIFO order if this case
# is true. The code should not have any more problems