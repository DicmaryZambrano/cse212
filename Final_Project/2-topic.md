# What is a Linked List?

A linked list is a linear data structure, which consists of a sequence of nodes. Each nodes contains a value and a pointer (a reference) to the next or previous node in the sequence. The first node we will be calling the head and the last node will be called the tail.

Imagine you have a playlist of songs that you want to organize. Each song can be represented as a node in a linked list, with two main components: the song itself (represented by data) and a pointer to the next song in the playlist. The first song in the playlist is the head of the linked list.

![Example of a linked list as a playlist](https://i.imgur.com/eSNfJDk.png)

The way linked lists are connected makes removing or changing elements around more efficient, elements in separate nodes that are linked together using pointers can be changed dynamically without needing to move the entire list in the memory. And when elements are added or removed from a linked list, only the more relevant nodes need to be modified to update the links between them. This makes them more efficient than dynamic arrays when removing elements.

However, you have to also take in consideration that linked lists can be less efficient than dynamic arrays when it comes to random access of elements, since they require traversing the list one node at a time to reach the elements. While dynamic arrays allow instant access to any element using an index.

## Types of Linked Lists

Here are some common types of linked lists:

- Singly Linked Lists: The simplest form on a linked list, every node contains a pointer to the next node and some data. Wich means it is unidirectional, you can only move in a single direction.

- Doubly Linked Lists: In this type of list each node contains data and a pointer both for the next node and the previous node. The movement is bi-directional, you can move in two directions

- Circular Linked Lists: Like with the singly linked list the node only contains a pointer to the next node and some data but the last node points back to the head node.

- Circular Doubly Linked Lists: Like with the doubly linked list the node each node contains data and a pointer both for the next node and the previous node, and like the circular linked list the last node will also point back to the head node.

Overall, understanding the different types of linked lists and their properties can be useful in choosing the appropriate data structure for a particular problem or application. In this tutorial we will be working with doubly linked list to solve real life problems.

## Basic Operations on Linked Lists (Insertion, Deletion, Traversal)

There are many operations we can perform on a linked list, like the typical insert, remove, and search operations. But you might find it interest how some operations have a better Big O performance than others. We will go thought each operation and explain why this is.

| Operation | Example                      | Description                                                                                  |
| --------- | ---------------------------- | -------------------------------------------------------------------------------------------- |
| Insertion | `linked_list.insert (item)`  | Adds a node to the linked list.                                                              |
| Deletion  | `linked_list.delete (item)`  | Removes a node from the linked list.                                                         |
| Search    | `linked_list.search(item)`   | Searches for a value in the linked list, returns true if it exists, returns false otherwise. |
| Size      | `linked_list.size()`         | Returns the size of the linked list.                                                         |
| Replace   | `linked_list.replace(value)` | Replaces the values of a node with the value introduced.                                     |
| Clear     | `linked_list.clear()`        | Clears the contents of the linked list.                                                      |

### Traversal

Just like with a dynamic array traversing trough the linked list takes a time complexity of O(n) because we have to go through every single node inside of the list. We can traverse trough the list thanks to the pointers that indicates us which element comes next until we find the tail.

![Image of a linked list with 4 songs](https://i.imgur.com/60WuwpD.png)

### Search

When we need to search for a certain value inside of the linked list, we have to use traversal to find the corresponding node where the value we are searching is being stored. This is why searching has a time complexity of O(n) instead of the O(1) dynamic arrays have.

### Insertion

When adding a new node inside of the linked list the time complexity depends of the position of insertion:

- Insertion at the head: will be O(1) because we only need to change the pointers on the head
- Insertion at the tail: will be O(1) because we only need to change the pointers on the tails
- Insertion at a specific point: is O(n) because we will need to traverse trough the linked list to find the position where we need to insert.

This is something that is easier to understand visually, imagine you have this situation, you have a new node that can’t go anywhere and you want to insert it after song 2. But song 2 in pointing to song 4 and song 4 point back to song 2.

![Example of insertion](https://i.imgur.com/atrCnuq.jpg)

The first step will be to connect song 3 to song 2 and 4. Still without disconnecting the song 2 and song 4 pointers.

![Example of insertion new node gets connected](https://i.imgur.com/DrxqCaJ.jpg)

Once song 3 is connected we now have to change the pointers of the adjacent nodes so they point to the new node. For song 2 we update the pointer that point to the next node, and for song 4 we update the pointer that point to the previous node.

![Example of insertion we update the pointers](https://i.imgur.com/aRH6G3B.jpg)

The same principle is applied to the head and the tails.

![Example of insertion figire to head or tail 1](https://i.imgur.com/BQhaAag.jpg)

![Example of insertion figire to head or tail 2](https://i.imgur.com/8CC2qmO.jpg)

![Example of insertion figire to head or tail 3](https://i.imgur.com/fCUkoo1.jpg)

### Deletion

Just like with Insertion, the performance of the Deletion will depend of the position of deletion

- Deletion at the head: will be O(1) because we only need to change the pointers on the head
- Deletion at the tail: will be O(1) because we only need to change the pointers on the tails
- Deletion at a specific point: is O(n) because we will need to traverse trough the linked list to find the position of the node we need to delete.

Let’s visualize this:

![Example of deletion](https://i.imgur.com/RKHIXdB.jpg)

Once we have found the node that we want to delete we will need to change the pointers of the adjacent nodes so they point to each other instead of pointing to the current node

![Example of deletion we connect the nodes](https://i.imgur.com/jFrphyE.jpg)

Now that the adjacent nodes are pointed to each other we can change the pointers of the node that we want to delete so it points nowhere.

![Example of deletion we make the node point nowhere](https://i.imgur.com/2gMx8EP.jpg)

The same principles apply to deleting the head and tail only that we just have to change the tail or head pointers, and because we already have access to the head and tail, we don’t need to traverse the linked list.

There can be many more operations but for now we will just work with the basics.

## Linked Lists in Python

There are some libraries that already build linked lists for you, but this time we will be building one from scratch. We will be creating two Classes, a LinkedLists class and a Node class that we can access inside of the LinkedList class.

The node class will create a node object with the attributes previous, next and store a value or more.

The Linked List class will store the head node, the tail node and keep track of how many nodes have been added, we don’t need to keep track of anything else because the nodes with connect to each other.

| Operation                       | Python Code                           | Performance | Description                                                                                  |
| ------------------------------- | ------------------------------------- | ----------- | -------------------------------------------------------------------------------------------- |
| Insertion after a certain point | `linked_list.insert (position, item)` | O(n)        | Adds a node to the linked list.                                                              |
| Insertion at head               | `linked_list.insert_head(item))`      | O(1)        | Adds a node at the head of the linked list.                                                  |
| Insertion at tail               | `linked_list.insert_tail(item)`       | O(1)        | Adds a note at the tails of the linked list.                                                 |
| Deletion                        | `linked_list.delete (item)`           | O(n)        | Removes a node from the linked list. O(1) if it’s the tail or head.                          |
| Search                          | `linked_list.search(item)`            | O(n)        | Searches for a value in the linked list, returns true if it exists, returns false otherwise. |
| Size                            | `linked_list.size()`                  | O(1)        | Returns the size of the linked list.                                                         |
| Replace                         | `linked_list.replace(value)`          | O(n)        | Replaces the values of a node with the value introduced. O(1) if it’s the tail or head.      |

By using classes, we get a lot of liberty on how we can manage the values on our linked list.

## Real life application for Linked Lists (Example problem)

Time for the next exercise! We might want to have a little fun with this one, lest say you want to create a music playlist so you can hear all your favorite songs. A linked list would be perfect for you because the playlist will keep track of the order of the songs.

![Person thinking about a playlist](https://i.imgur.com/ZlL9Hsl.jpg)

Your playlist should include the following:

- Add(song): Add a song to your linked list
- Remove(song): remove a song from your linked list
- Play (): Prints out all the songs that are in your linked list in order.

It should also follow these rules:

- Each node in the linked list contains a song.
- When adding a new song, it should be added at the tails of the linked list.
- When removing a song, only the first occurrence of the task should be removed.
- When you “play” the songs they would be printed out in the order in which they were added and at the top it should say how many songs there are.

Lest start by creathing the classes for our music playlist:

```python
class MusicPlaylist:
    class SongNode:
        def __init__(self, song, prev=None, next=None):
            """
            Initializes a new node with the given `song`, `prev` node, and `next` node.

            Args:
                song: The song to be stored in the node.
                prev: The previous node in the linked list. Defaults to None.
                next: The next node in the linked list. Defaults to None.
            """
            self.song = song
            self.prev = prev
            self.next = next

    def __init__(self):
        """
        Initializes an empty music playlist.
        """
        self.head = None  # Initialize the head of the linked list to None
        self.tail = None  # Initialize the tail of the linked list to None
        self.num_songs = 0  # Initialize the number of songs in the playlist to 0
```

We first need to implement the add function, so we can add new songs to our playlist remeber that we want to add song to the tail of the playlist

```python
    def add(self, song):
        """
        Adds a new song to the tail of the music playlist.
        """
        new_node = self.SongNode(song, self.tail, None)  # Create a new node with the given song
        if self.tail:
            self.tail.next = new_node  # If the tail already exists, set its next attribute to the new node
        else:
            self.head = new_node  # If the tail doesn't exist, set the head attribute to the new node
        self.tail = new_node  # Set the tail attribute to the new node
        self.num_songs += 1  # Increment the number of songs in the playlist
```

Next step is to implement the remove functions.

Lets first create some helper functions to make our code cleaner, like functions to remove the head or tail.

```python
    def remove_head(self):
        """
        Removes the head node from the music playlist.
        """
        if self.head is None:
            # If the playlist is empty, do nothing
            return

        if self.head.next is None:
            # If there's only one node in the playlist, set both head and tail to None
            self.head = None
            self.tail = None
        else:
            # Otherwise, remove the head node and update the head
            self.head = self.head.next
            self.head.prev = None
        self.num_songs -= 1

    def remove_tail(self):
        """
        Removes the tail node from the music playlist.
        """
        if self.tail is None:
            # If the playlist is empty, do nothing
            return

        if self.tail.prev is None:
            # If there's only one node in the playlist, set both head and tail to None
            self.head = None
            self.tail = None
        else:
            # Otherwise, remove the tail node and update the tail
            self.tail = self.tail.prev
            self.tail.next = None
        self.num_songs -= 1
```

Good job, now with these functions we can implement our remove function.

```python
    def remove(self, song):
        """
        Removes the first occurrence of a song from the music playlist.
        """
        node = self.head  # Start at the head of the linked list

        while node is not None:
            # If we find the node with the given song
            if node.song == song:
                # If the node to remove is the head, use remove_head helper function
                if node == self.head:
                    self.remove_head()

                # If the node to remove is the tail, use remove_tail helper function
                elif node == self.tail:
                    self.remove_tail()

                # Otherwise, remove the node from the playlist by updating the links
                else:
                    node.prev.next = node.next
                    node.next.prev = node.prev
                    self.num_songs -= 1

                # Break the loop
                break

            node = node.next  # Move to the next node in the linked list
```

Perfect! Everything is set up so we can start playing our songs, let's create the play function so it prints the number of songs and the names of each song

```python
    def play(self):
        """
        Iterates over the music playlist and prints out all the songs in order.
        """
        print(f"Now playing {self.num_songs} songs:")
        node = self.head  # Start at the head of the linked list
        while node:
            print(node.song)  # Print the song stored in the current node
            node = node.next  # Move to the next node in the linked list
```

This should be good enough, let look at the full code!

```python
'''
You wanted to create a cool playlist to store your favorite songs.
so you decided to create a Linked List that stores all you songs
in a playlist.
'''

class MusicPlaylist:
    class SongNode:
        def __init__(self, song, prev=None, next=None):
            """
            Initializes a new node with the given `song`, `prev` node, and `next` node.

            Args:
                song: The song to be stored in the node.
                prev: The previous node in the linked list. Defaults to None.
                next: The next node in the linked list. Defaults to None.
            """
            self.song = song
            self.prev = prev
            self.next = next

    def __init__(self):
        """
        Initializes an empty music playlist.
        """
        self.head = None  # Initialize the head of the linked list to None
        self.tail = None  # Initialize the tail of the linked list to None
        self.num_songs = 0  # Initialize the number of songs in the playlist to 0

    def add(self, song):
        """
        Adds a new song to the tail of the music playlist.
        """
        new_node = self.SongNode(song, self.tail, None)  # Create a new node with the given song
        if self.tail:
            self.tail.next = new_node  # If the tail already exists, set its next attribute to the new node
        else:
            self.head = new_node  # If the tail doesn't exist, set the head attribute to the new node
        self.tail = new_node  # Set the tail attribute to the new node
        self.num_songs += 1  # Increment the number of songs in the playlist


    def remove(self, song):
        """
        Removes the first occurrence of a song from the music playlist.
        """
        node = self.head  # Start at the head of the linked list

        while node is not None:
            # If we find the node with the given song
            if node.song == song:
                # If the node to remove is the head, use remove_head helper function
                if node == self.head:
                    self.remove_head()

                # If the node to remove is the tail, use remove_tail helper function
                elif node == self.tail:
                    self.remove_tail()

                # Otherwise, remove the node from the playlist by updating the links
                else:
                    node.prev.next = node.next
                    node.next.prev = node.prev
                    self.num_songs -= 1

                # Break the loop
                break

            node = node.next  # Move to the next node in the linked list

    def remove_head(self):
        """
        Removes the head node from the music playlist.
        """
        if self.head is None:
            # If the playlist is empty, do nothing
            return

        if self.head.next is None:
            # If there's only one node in the playlist, set both head and tail to None
            self.head = None
            self.tail = None
        else:
            # Otherwise, remove the head node and update the head
            self.head = self.head.next
            self.head.prev = None
        self.num_songs -= 1

    def remove_tail(self):
        """
        Removes the tail node from the music playlist.
        """
        if self.tail is None:
            # If the playlist is empty, do nothing
            return

        if self.tail.prev is None:
            # If there's only one node in the playlist, set both head and tail to None
            self.head = None
            self.tail = None
        else:
            # Otherwise, remove the tail node and update the tail
            self.tail = self.tail.prev
            self.tail.next = None
        self.num_songs -= 1


    def play(self):
        """
        Iterates over the music playlist and prints out all the songs in order.
        """
        print(f"Now playing {self.num_songs} songs:")
        node = self.head  # Start at the head of the linked list
        while node:
            print(node.song)  # Print the song stored in the current node
            node = node.next  # Move to the next node in the linked list


# Create a new music playlist
playlist = MusicPlaylist()

# Add some songs to the playlist
playlist.add("Song 1")
playlist.add("Song 2")
playlist.add("Song 3")

# Remove a song from the playlist
playlist.remove("Song 2")

# Add some more songs to the playlist
playlist.add("Song 4")
playlist.add("Song 5")

# Play the songs in the playlist
playlist.play()
```

After tweaking and organizing your playlist you now have the ultimate playlist full of your favorite songs, and also have a way to remove some songs if you get tired of them. Good job on your linked list!

![Happy person listening to music](https://i.imgur.com/mjDsOmE.jpg)

## Example Problem

Now it is time for you to solve the next problem, this time we will be working with multiple values on our linked list to create a shopping list.

You have been tasked with implementing a shopping cart application using a linked list. Your application should allow the user to add, remove, and view items in their shopping cart.

hints: you can add more than a single attribute to your nodes, and don't forget to update the total prices
and the total number of items. Use the previous linked list as a template to complete the missing code

Your implementation should include the following:

- add(target_item,item, price): Adds a new afther the target item.

- add_to_tail(item, price): Adds an item to the tail of the list.

- add_to_head(item, price): Adds an item to the head of the list.

- remove(item): Removes the first occurrence of the given item from the linked list, if it exists.

- remove_head(item): Removes from the head.

- remove_tail(item): Removes from the tail.

- view(): Prints out all the items in the linked list, along with their prices and the total cost of the shopping cart.

Your implementation should also adhere to the following rules:

- Each node in the linked list should contain a single item (i.e., a string) and its price.

- When adding a new item, you can add at a certain target, add to the tail or add to the head.

- When removing an item, only the first occurrence of the item should be removed.

- When viewing the shopping cart, the items and their prices should be printed out, as well as the total cost of the shopping cart.

- Once you have implemented the linked list, you should be able to efficiently add, remove, and view items in the shopping cart.

copy the code below to start working on your solution, compare your solution to [this example solution](/python/02-shopping_list_solution.py).

```python
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

    def __init__(self):
        """
        Initializes an empty shopping cart.
        """
        self.head = None  # Initialize the head of the linked list to None
        self.tail = None  # Initialize the tail of the linked list to None

        # Initialize the number of items in the shopping cart to 0
        # Initialize the total cost of the shopping cart to 0

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

        # Increment the number of items in the shopping cart
        # Add the price of the new item to the total cost

    def add_to_tail(self, item, price):
        """
        Adds a new item to the end of the shopping cart.
        """
        new_node = self.ItemNode(item, price, self.tail, None)  # Create a new node with the given item and price
        if self.tail is None:
            # If the shopping cart is empty, set both the head and tail to the new node
            pass
        else:
            # Otherwise, insert the new node after the tail
            pass

        # Increment the number of items in the shopping cart
        # Add the price of the new item to the total cost

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
                    # use the previous functions you created for your solution
                    pass
                node.next = new_node
                if new_node.next is None:
                    # use the previous functions you created for your solution
                    pass

                # Increment the number of items in the shopping cart
                # Add the price of the new item to the total cost

                # Break the loop
                return

            node = node.next

        # If we get here, we didn't find the target item in the shopping cart

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
            #fill in your solution
            pass
        else:
            #fill in your solution
            pass

        # decrease the number of items in the shopping cart
        # subtract the price of the new item to the total cost

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
            #fill in your solution
            pass
        else:
            #fill in your solution
            pass

        # Decrement the number of items in the shopping cart
        # Subtract the price of the new item to the total cost

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
                    pass
                    # Decrement the number of items in the shopping cart
                    # Subtract the price of the removed item from the total cost
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
                #fill in your solution
                pass
            print(f"Total cost: ${self.total_cost:.3}")

# Create a new shopping cart
cart = ShoppingCart()

# Test adding items to the shopping cart
cart.add_to_tail("Banana", 0.99)
cart.add_to_tail("Apple", 1.29)
cart.add_to_head("Orange", 0.79)

# Test viewing the shopping cart
cart.view()

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

# Expected output:
# Shopping cart:
# Orange: $0.79
# Banana: $0.99
# Total cost: $1.78

# Test removing a non-existent item from the shopping cart
cart.remove("Grape")

# Test viewing the shopping cart again
cart.view()

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

# Expected output:
# Shopping cart:
# Pineapple: $2.99
# Grape: $1.99
# Total cost: $4.98

# Create more test cases if you want
```
