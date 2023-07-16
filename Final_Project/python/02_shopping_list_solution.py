'''
You have been tasked with implementing a shopping cart application 
using a linked list. Your application should allow the user 
to add, remove, and view items in their shopping cart. And also
be able to view the total price on of their list
'''

class ShoppingCart:
    class ItemNode:
        def __init__(self, item, price, prev=None, next=None):
            """
            Initializes a new node with the given `item`, `price`, `prev` node, and `next` node.
            """
            self.item = item
            self.price = price
            self.prev = prev
            self.next = next

    def __init__(self):
        """
        Initializes an empty shopping cart.
        """
        self.head = None  # Initialize the head of the linked list to None
        self.tail = None  # Initialize the tail of the linked list to None
        self.num_items = 0  # Initialize the number of items in the shopping cart to 0
        self.total_cost = 0  # Initialize the total cost of the shopping cart to 0

    def add_to_head(self, item, price):
        """
        Adds a new item to the beginning of the shopping cart.
        """
        new_node = self.ItemNode(item, price, None, self.head)  # Create a new node with the given item and price
        if self.head is None:
            # If the shopping cart is empty, set both the head and tail to the new node
            self.head = new_node
            self.tail = new_node
        else:
            # Otherwise, insert the new node before the head
            self.head.prev = new_node
            self.head = new_node
        self.num_items += 1  # Increment the number of items in the shopping cart
        self.total_cost += price  # Add the price of the new item to the total cost

    def add_to_tail(self, item, price):
        """
        Adds a new item to the end of the shopping cart.
        """
        new_node = self.ItemNode(item, price, self.tail, None)  # Create a new node with the given item and price
        if self.tail is None:
            # If the shopping cart is empty, set both the head and tail to the new node
            self.head = new_node
            self.tail = new_node
        else:
            # Otherwise, insert the new node after the tail
            self.tail.next = new_node
            self.tail = new_node
        self.num_items += 1  # Increment the number of items in the shopping cart
        self.total_cost += price  # Add the price of the new item to the total cost

    def add(self, target_item, new_item, new_price):
        """
        Inserts a new item with the given name and price after the first occurrence of the specified target item in the
        shopping cart, if it exists.
        """
        node = self.head  # Start at the head of the linked list

        while node is not None:
            if node.item == target_item:  # If we find the node with the given item
                new_node = self.ItemNode(new_item, new_price)  # Create a new node with the given item and price
                new_node.prev = node
                new_node.next = node.next
                if node.next is not None:
                    node.next.prev = new_node
                node.next = new_node
                if new_node.next is None:
                    self.tail = new_node
                self.num_items += 1  # Increment the number of items in the shopping cart
                self.total_cost += new_price  # Add the price of the new item to the total cost

                # Break the loop
                return

            node = node.next

        # If we get here, we didn't find the target item in the shopping cart
        print(f"Item '{target_item}' not found in shopping cart, cant add '{new_item}' to the list")

    def remove_head(self):
        """
        Removes the head node from the shopping cart.
        """
        if self.head is None:
            # If the shopping cart is empty, do nothing
            return
        removed_node = self.head

        self.head = removed_node.next
        if self.head is not None:
            self.head.prev = None
        else:
            self.tail = None
        self.num_items -= 1
        self.total_cost -= removed_node.price

    def remove_tail(self):
        """
        Removes the tail node from the shopping cart.
        """
        if self.tail is None:
            # If the shopping cart is empty, do nothing
            return
        removed_node = self.tail

        self.tail = removed_node.prev
        if self.tail is not None:
            self.tail.next = None
        else:
            self.head = None
        self.num_items -= 1
        self.total_cost -= removed_node.price

    def remove(self, item):
        """
        Removes the first occurrence of the given item from the shopping cart, if it exists.

        Args:
            item: The name of the item to be removed from the shopping cart.
        """
        node = self.head  # Start at the head of the linked list

        while node is not None:
            if node.item == item:  # If we find the node with the given item
                if node == self.head:
                    # If the node to remove is the head, remove the head
                    self.remove_head()
                elif node == self.tail:
                    # If the node to remove is the tail, remove the tail
                    self.remove_tail()
                else:
                    # Otherwise, remove the node from the shopping cart by updating the links
                    node.prev.next = node.next
                    node.next.prev = node.prev
                    self.num_items -= 1  # Decrement the number of items in the shopping cart
                    self.total_cost -= node.price  # Subtract the price of the removed item from the total cost
                return
            node = node.next

    def view(self):
        """
        Prints out all the items in the shopping cart, along with their prices and the total cost of the shopping cart.
        """
        if self.head is None:
            # If the shopping cart is empty, print a message indicating that
            print("Your shopping cart is empty.")
        else:
            # Otherwise, iterate over the linked list and print out the items and their prices
            print("Shopping cart:")
            node = self.head
            while node is not None:
                print(f"{node.item}: ${node.price}")
                node = node.next
            print(f"Total cost: ${self.total_cost:.3}")

# Create a new shopping cart
cart = ShoppingCart()

# Test adding items to the shopping cart
cart.add_to_tail("Banana", 0.99)
cart.add_to_tail("Apple", 1.29)
cart.add_to_head("Orange", 0.79)

# Test viewing the shopping cart
cart.view()
print("\n======================")
# Expected output:
# Shopping cart:
# Orange: $0.79
# Banana: $0.99
# Apple: $1.29
# Total cost: $3.07

# Test removing an item from the shopping cart
cart.remove("Apple")

# Test viewing the shopping cart again
cart.view()
print("\n======================")
# Expected output:
# Shopping cart:
# Orange: $0.79
# Banana: $0.99
# Total cost: $1.78

# Test removing a non-existent item from the shopping cart
cart.remove("Grape")

# Test viewing the shopping cart again
cart.view()
print("\n======================")
# Expected output:
# Shopping cart:
# Orange: $0.79
# Banana: $0.99
# Total cost: $1.78

# Test adding more items to the shopping cart afther the Banana item
cart.add("Orange","Grape", 1.99)
cart.add("Orange","Pineapple", 2.99)

# Test viewing the shopping cart again
cart.view()
print("\n======================")
# Expected output:
# Shopping cart:
# Orange: $0.79
# Pineapple: $2.99
# Grape: $1.99
# Banana: $0.99
# Total cost: $6.76

# Test removing items from the head and tail
cart.remove_head()
cart.remove_tail()

# Test viewing the shopping cart again
cart.view()
print("\n======================")
# Expected output:
# Shopping cart:
# Pineapple: $2.99
# Grape: $1.99
# Total cost: $4.98

# Create more test cases if you want