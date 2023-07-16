# What is a Binary Search Tree?

A binary search tree is a type of data structure that uses nodes to store and organize data. Similar to a linked list, it consists of nodes, but instead of following a linear path, it mimics the branches of a tree. It's called a "binary" tree because each node can have at most two child nodes. It's called a "search" tree because it allows us to quickly search for a specific value in the tree.

At the top of the tree is the root node, also known as the parent node, the root node branches out into two or fewer child nodes also called sub trees. Each child node can also have two or fewer child nodes branching out from it, and so on until we find children nodes with no other child nodes connected to them, called the leaves.

As a result, the binary search tree looks like the branches of a tree, with the root node at the top and the child nodes branching out from it into leaves:

![Example of a binary tree structure](https://i.imgur.com/EdhymGO.jpg)

One important rule of binary search trees is that the values of the nodes in the left subtree are always less than the value of the root node, and the values of the nodes in the right subtree are always greater than the value of the root node. This ordering property allows us to search the tree efficiently.

This ordering property allows for efficient search operations on the tree. When searching for a specific value, we can use the ordering property to quickly eliminate entire subtrees based on the values stored in their root nodes. This makes searching in a binary search tree very efficient, with an average-case time complexity of O(log n) when the tree is balanced. This means that we are essentially "cutting in half" the remaining nodes that we need to search.

In this example where we are looking for a node that contains 30 we can see this principle in action:

![Example of searching a value 1](https://i.imgur.com/E5GMy6b.jpg)
![Example of searching a value 2](https://i.imgur.com/dnfuo2R.jpg)
![Example of searching a value 3](https://i.imgur.com/FtVXaWW.jpg)

Each comparison eliminates half of the remaining nodes that need to be searched. This is very efficient compared to linear search O(n) that would be required if the data was stored in an unsorted list or array.

However, this is the case when the binary search tree is organized, an unorganized binary search tree will probably have a time complexity of O(n). Like in the example below were we want to search for 7, one branch is significantly taller that the other branch, and the values are not being distributed properly

![Example of an unorganized binary tree](https://i.imgur.com/Q3SEcoG.jpg)

It is very important to take this into consideration when creating your tree.

## Types of Binary Search Trees

Just like queues and linked lists there are many types of binary trees. But binary search trees are usually categorized by the number of children and the difference in dept between the branches.

- Balanced BST: In a balanced binary search tree, the height of the tree is kept relatively low and balanced, ensuring that operations such as search, insert, and delete have a time complexity of O(log n) in the worst case. Self-balancing binary search trees, such as AVL trees and Red-Black trees, automatically adjust their structure to maintain balance and keep the height of the tree low.

- Unbalanced BST: An unbalanced binary search tree has a height that can become very large, resulting in operations that take longer to complete. This can occur when the tree is constructed in an unbalanced way, or when elements are inserted or removed in a way that disrupts the balance of the tree. In the worst case, operations on an unbalanced binary search tree can have a time complexity of O(n).

- Perfect BST: A perfect binary tree is a binary tree in which all internal nodes have exactly two children, and all leaf nodes are at the same level or depth. A perfect binary tree of height h has 2^(h+1) - 1 nodes. Perfect binary trees are useful in certain algorithms and data structures, as their structure can be exploited to achieve efficient space and time complexity.

In our tutorial we will try to keep our BST as balanced as we can possibly get them.

## What is Recursion

Before we can move on to the basic operations on BST, we will have to talk about a pretty important concept on programming, recursion.

Recursion is a programming technique that involves a function calling itself. This can be useful for solving problems that involve repetitive or self-similar structures. However, if the function keeps calling itself indefinitely, it can lead to an error.

```python
def f(x):
    return f(x-1) #this function will call itself infinitely
```

To prevent this, we use a base case, which is a condition that tells the function when to stop calling itself. If the base case is not met, the function will keep calling itself recursively. Once the base case is met, the recursion stops, and the function returns a result.

```python
def f(x):
    if x==0:
        return 1 #this is the base case

    return 1 + f(x-1) #the function will be called until the base case is met
```

The result of a function like this can be a little hard to comprehend so it is very useful to visualize each step of the process to really understand what is happening here

![Example of recursion 1](https://i.imgur.com/u6NEOxR.jpg)

in step 1 we are calling the function for the first time with the value of 1, because 1 does not satisfy the base case we call the same function again with the values of 1-1 or 0

in step 2 0 does satisfy the base case so instead of calling itself again with the value of -1 it will return 1.

in step 3 we start evaluating the returns, f(1-1) returned 1 so now f(1) can evaluate 1+1 which is equal to 2 in the final step.

Les't look at another example where instead of calling the same function once we call it two times

```python
def f(x):
    if x<1:
        return 1 #this is the base case

    return f(x-1) + f(x-1) #the function will be called until the base case is met
```

Now what do you imagine is going to happen in this recursive function?

In the first step we will evaluate f(1), because 1 is not lower than 1 the base case hasn't been met so we call f(1-1), and then we call f(1-1) a second time. They might look the same but these are two different calls.

![Example of recursion 2](https://i.imgur.com/buqX9mY.jpg)

The two calls will go trough the same steps and they both satisfy the base case so they return 1

![Example of recursion 3](https://i.imgur.com/BO0jkYQ.jpg)

Finally f(1) can evaluate 1 + 1 and return a value of 2. Now that we have a basic idea of how recursive functions are called let's look at how we can solve real life problem using recursion.

### The fibonacci sequence

The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding numbers, starting from 0 and 1. For example, the sequence goes 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, and so on.

To calculate the nth number in the Fibonacci sequence using recursion, we need to define a base case that stops the recursion. In this case, we can say that if n is 0 or 1, the function should return n, because these are the only two values for which we can directly calculate the corresponding Fibonacci number without having to recursively call the function.

This would leave us with something like this:

```python

def fibonacci(n):
    if n <= 1:
        return n #if number is 0 or 1 return it

```

Once we have our base case, we can define our recursive function to calculate the nth Fibonacci number. We do this by adding the values of the previous two Fibonacci numbers, which we can get by recursively calling our function with n-1 and n-2 as arguments.

```python

return fibonacci(2-1) + fibonacci(2-2)

return 0 + 1

return 1

```

Basically we need to subtract from the number until we get the sum 0 + 1, this will unravel until we get the desired fibonacci number that corresponds to the position we entered.

```python

def fibonacci(n):
    if n <= 1:
        return n # returns 0 or 1
    else:
        return fibonacci(n-1) + fibonacci(n-2) # two different recursive calls

result_1 = fibonacci(5)
result_2 = fibonacci(8)

print(result_1)  # Output: 5
print(result_2)  # Output: 21

```

To make it easier to understand, we can visualize this process as a tree, where each node represents a call to the Fibonacci function with a particular value of n, and the branches represent the recursive calls to the function with n-1 and n-2 as arguments.

![Example of recursion 3](https://i.imgur.com/a2dXh45.jpg)

You might notice how similar this looks to the structure of the BST, for this tutorial we will be solving the basic operations of a BST by using recursion. It is completely ok if you can't grasp this concept fully, you will come to understand recursion better as you practice and solve problems with it.

### The performance of recursion

Although recursion can be a powerful tool for solving complex problems we need to understand how it works in terms of performance.

When we use recursion, we call the same function multiple times with different input values, and each function that is called created a new instance of itself on the call stack, this data structure keeps track of the order in which function calls are made. As a result recursion can use a lot of memory and processing power, specially when dealing with large input values.

However, recursion can also be more elegant and easier to understand that iterative solutions in certain cases, specially when dealing with complex data structures or algorithms like binary search trees.

A way we can improve the performance of our recursive functions is by caching the result of the function calls so that they can be reused later. In the case of the Fibonacci function, memoization can be used to avoid redundant calculations of Fibonacci numbers that have already been computed.

```python

# create an empty dictionary to store the results of previous function calls
memo = {}

def fibonacci(n):
    # check if the result has already been computed and stored in the memo
    if n in memo:
        return memo[n]

    # compute the Fibonacci number recursively and store the result in the memo
    if n <= 1:
        memo[n] = n
    else:
        memo[n] = fibonacci(n-1) + fibonacci(n-2)

    # return the result
    return memo[n]

```

Without memoization, the Fibonacci function has an exponential time complexity of O(2^n), but with memoization, the time complexity is reduced to O(n), which is much more efficient.

## Basic Operations on BST

Just like the data structures we have studied before, you can insert nodes into the BST, search for a node, delete a node, traverse trough the BST in order or pre order. In this table below we list some of the expected time complexities if the binary search tree is balanced:

| Operation                | Time Complexity | Description                                                                                                                                         |
| ------------------------ | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `insert(value, node)`    | O(log n)        | Inserts a new node with the given `value` into the tree rooted at `node`.                                                                           |
| `search(value, node)`    | O(log n)        | Searches the tree rooted at `node` for the node with the given `value`. Returns the node if it exists, otherwise returns `None`.                    |
| `delete(value, node)`    | O(log n)        | Deletes the node with the given `value` from the tree rooted at `node`, if it exists. Returns the root of the updated tree.                         |
| `height(node)`           | O(n)            | Returns the height of the tree. The height of a tree is the maximum depth of any node in the tree + 1 to account for the root.                      |
| `size(node)`             | O(1)            | Returns the number of nodes in the tree rooted at node.                                                                                             |
| `traverse_inorder(node)` | O(n)            | Traverses the tree rooted at node in inorder fashion (left subtree, root, right subtree), and returns a list of the node values in ascending order. |

### Traversal

In order to traverse trough a BST we use the same method as the one we used with the linked lists, because each node has a pointer we can simply point to the left or right node until we reach a leaf or we find what we are looking for, depending on what you need to do the expected time complexity of traversing thorough the tree will be of O(log n) in organized trees and O(n) in the worst case scenario

![Example of traversal](https://i.imgur.com/9vi1AvL.jpg)

### Insertion

In the case of inserting a value inside a binary search tree we have to remember how the tree is structure, the values of the left node will be greater than the values on the right node. We will traverse the node using this logic until we find an empty spot where we can insert our new node, the only thing we would have to do is to connect the nodes

![Example of insertion](https://i.imgur.com/10AiP8g.jpg)

### Deletion

This operation can be a bit more complex depending of the number of children the node you want to delete has, it requires some clean up to maintain the structure of the binary search tree, in this tutorial we will only create a function to delete nodes with no children or nodes with only one child.

If the node exists and has no children we just can simply delete it by setting the node to none

![Example of delete](https://i.imgur.com/Ux5q0K0.jpg)

If the node exists and has one child we can replace it by its own child

![Example of delete and replace](https://i.imgur.com/3eaRKBE.jpg)

If the node has two children we need to find the minimum node in the right subtree, replace the current node's value with the minimum value, and recursively delete the minimum node from the right subtree.

![Example of delete and organize](https://i.imgur.com/faWUDZt.jpg)

### Height

To find the height of the BST we will need to compare the heigh of each branch until we find the longest one, the length of the longest branch + 1 will give us the height of the tree. You could use recursion to traverse trough each branch

![Example of height](https://i.imgur.com/7gc5Xf6.jpg)

## BST in Python

Just like with the linked list we will be using classes to create Binary search tree objects that will keep track of all the nodes and methods.

Each nodes will store a value and a pointer to the left and the right.

Instead of using regular loops we will be using recursion to solve each one of these operations so you will have plenty of opportunities to apply what you have learned

Now lest's discuss how we can apply the comparisons between nodes to decide their position with something else besides just numbers. We are aware that 35 is greater than 20, but what i we need to organize people by their names? what is we need to organize phone numbers?

We could create out own logic to determine which one is greater but Python has it's own built in logic to compare strings, what do you think would happen if we ran this piece of code?

```python

compare = "This" > "That"

print(compare)

#option 1: error
#option 2: true
#options 3: false

```

If we run this piece of code we will find that it prints `true`, what is happening here? Let's step through the comparison of the strings "This" and "That" in Python:

- The comparison This > That is evaluated in Python.

- Python compares the first character of each string, "T" and "T". Since they are the same, Python moves on to the second character of each string.

- Python compares the second character of each string, "h" and "a". Since "h" has a larger Unicode code point than "a", Python determines that "This" is greater than "That" and the comparison evaluates to True.

- Python stops comparing the strings and returns the result of the comparison, which is True.

The logic behind this comparison is that Python is comparing the Unicode code points of each character in the strings. In this case, the code point of "h" (104) is greater than the code point of "a" (97), so "This" is considered greater than "That". If the first characters had been different, Python would not have compared any further characters and would have determined the result based on the comparison of the first characters.

Now, what will happen if we run this piece of code?

```python

compare = "2" > "10"

print(compare)

#option 1: error
#option 2: true
#options 3: false

```

At first we might intuitively conclude that "2" is not greater than "10" but the result that gets printed actually `true`. The reason for the incorrect result is that Python is comparing the strings as text, not as numbers. When comparing strings as text, "2" is considered greater than "10", because "2" (50) has a larger Unicode code point than "1" (49), which is the first digit in "10".

Now that we've seen how we can use a binary search tree to store data other than numbers, let's explore the potential applications of this approach by solving a problem that involves storing and retrieving non-numeric data. By using a binary search tree to organize and search our data, we can make our code more efficient and engaging for the user.

## Real life application for a Binary Search Tree

Binary search trees are a powerful data structure that can be used to efficiently store and retrieve large amounts of data.

By using a binary search tree to store contact information, we can quickly search for and add new contacts, making it an ideal solution for managing a large address book or contact list.

![Troubled person looking at an unorganized contact book](https://i.imgur.com/ZW4uw6J.jpg)

Let's say you start looking at your contacts on your note book and start searching for the new number of your best friend, but
you have so many contacts in your note book that it takes you way too much time to go trough the contacts one by one,
your task it to create a fast and efficient way to organize your contacts in python to make it easier for you to find everything.

Requirements:

- The Contact class should have attributes for the name and phone number of each contact, as well as pointers to the left and right child nodes.

- The ContactBook class should have a root attribute that points to the root node of the binary search tree.

- The insert method should take a name and phone number as arguments, create a new Contact object with those values, and insert it into the binary search tree in the correct position based on the name, if a contact with the same name replace it with the new information.

- The search method should take a name as an argument and return True if a Contact object with that name exists in the binary search tree, or False otherwise.

- The delete method should take a name as an argument and delete the Contact object with that name from the binary search tree, if it exists and has no children.

- The display method should display all the Contact objects in the binary search tree in alphabetical order by name.

Lets start by creating our classes, the Contact class will be our nodes and the ContactBook will manage the root of the tree and all our methods

```python

class ContactBook:
    class Contact:
        def __init__(self, name, phone):
            self.name = name
            self.phone = phone
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None
```

Our first function will be the insert function, we will create a new node with the information that was provided, if the root is None this will be our new root node, if this is not the case we will need to traverse trough the tree until we find an empty spot, we can use a helper function to make things a bit cleaner.

This helper function will be the one to be called recursively so we need a base case, we know that if we hit a leaf node we should stop recursing because we have found an empty spot for our node, our insert functions wil look something like this:

```python

    def insert(self, name, phone):
        """
        Inserts a new Contact object into the binary search
        tree in alphabetical order by name.
        If a contact with the same name already exists,
        the method replaces the existing phone number with the new phone number.
        """
        new_contact = self.Contact(name, phone)
        if self.root is None:
            # If the binary search tree is empty,
            # the new Contact object becomes the root of the tree.
            self.root = new_contact
        else:
            # Otherwise, call the _insert_helper method to
            # recursively traverse the tree from the root to a leaf node.
            self._insert_helper(self.root, new_contact)

    def _insert_helper(self, current, new_contact):
        """
        A helper method for the insert method that recursively
        traverses the binary search tree to find the correct
        position to insert a new Contact object.
        """
        if new_contact.name == current.name:
            # If the name of the new Contact object matches the name
            # of the current node, replace the phone number of the
            # current node with the phone number of the new Contact object.
            current.phone = new_contact.phone

        elif new_contact.name < current.name:
            # If the name of the new Contact object is less
            # than the name of the current node, go left.
            if current.left is None:
                # If the current node does not have a left child,
                # insert the new Contact object as the left child.
                current.left = new_contact
            else:
                # Otherwise, recursively call the _insert_helper method
                # with the left child as the new current node.
                self._insert_helper(current.left, new_contact)
        else:
            # If the name of the new Contact object is greater
            # than the name of the current node, go right.
            if current.right is None:
                # If the current node does not have a right child,
                # insert the new Contact object as the right child.
                current.right = new_contact
            else:
                # Otherwise, recursively call the _insert_helper
                # method with the right child as the new current node.
                self._insert_helper(current.right, new_contact)

```

Now lets work on our search function, we need to traverse our tree just like with our insert function but this time we will return true if we find the contact we are looking for, or false if we hit a leaf node. The helper function will be the one to be called recursively, the base case should also be the same, if the left or right node is equal to none we should stop:

```python

    def search(self, name):
        """
        Searches the binary search tree for a Contact object with the specified name.
        Returns True if a Contact object with that name exists in the binary search tree, or False otherwise.
        """
        return self._recursive_search(self.root, name)

    def _recursive_search(self, current, name):
        """
        A recursive helper method for the search method that
        traverses the binary search tree to find the Contact object
        with the specified name.
        """
        if current is None:
            # If the method reaches a leaf node without finding a match, return False.
            return False
        elif name == current.name:
            # If the name of the current node matches the specified name, return True.
            return True
        elif name < current.name:
            # If the specified name is less than the name of the current node,
            # recursively call the _recursive_search method with the left child as the new current node.
            return self._recursive_search(current.left, name)
        else:
            # If the specified name is greater than the name of the current node,
            # recursively call the _recursive_search method with the right child as the new current node.
            return self._recursive_search(current.right, name)

```

The deletion function for this exercise will only delete nodes with no children, if you are wondering why we set the root to whatever our helper function returns, it is because when we delete a node, we may need to update the parent node's left or right child pointer to point to a new node. This may affect the root of the tree if the node being deleted is the root itself. Therefore, we need to update the root of the tree after deleting a node.

In the delete method, we call the `recursive_delete` method to delete the node with the specified name. Once we have deleted the node, we use self.root = to update the root of the binary search tree to the new root returned by the `recursive_delete` method. This ensures that the root of the tree always points to the correct node, even after deleting the old root.

```python

    def delete(self, name):
        """
        Calls the recursive delete method to delete a node only if it has no children
        """
        self.root = self._recursive_delete(self.root, name)

    def _recursive_delete(self, current, name):
        """
        A recursive helper method for the delete method
        """

        if current is None:
            return None
        elif name == current.name:
            if current.left is None and current.right is None:
                # If the current node has no children, delete it by returning None.
                return None
            else:
                # Otherwise, return the current node unchanged.
                return current
        elif name < current.name:
            current.left = self._recursive_delete(current.left, name)
        else:
            current.right = self._recursive_delete(current.right, name)
        return current

```

Finally we need a method to display all the contacts in our contact book in alphabetical order; Since the BST is ordered by name, we can print the names in alphabetical order by recursively traversing the left subtree first, starting from the lowest name in the tree, and then recursively traversing the right subtree, starting from the lowest name in the right subtree. This ensures that the names are printed in the correct order. By using this approach, we can print all the contacts in our contact book in a neat and organized way.

```python

    def display(self):
        """
        Calls the recursive display method to display all the contact information in order
        """
        if self.root is None:
            print("Contact book is empty.")
        else:
            self._display_helper(self.root)

    def _display_helper(self, current):
        """
        A recursive helper method for the display method
        """
        if current is not None:
            self._display_helper(current.left)
            print(f"Name: {current.name}, Phone: {current.phone}")
            self._display_helper(current.right)

```

Let's see how the full code would look like

```python

"""
    Let's say you start looking at your contacts on your note book and start searching
    for the new number of your best friend, but you have so many contacts in your note
    book that it takes you way too much time to go trough the contacts one by one, your
    task it to create a fast and efficient way to organize your contacts in python to
    make it easier for you to find everything.
"""
class ContactBook:
    class Contact:
        def __init__(self, name, phone):
            self.name = name
            self.phone = phone
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, name, phone):
        """
        Inserts a new Contact object into the binary search
        tree in alphabetical order by name.
        If a contact with the same name already exists,
        the method replaces the existing phone number with the new phone number.
        """
        new_contact = self.Contact(name, phone)

        if self.root is None:
            # If the binary search tree is empty,
            # the new Contact object becomes the root of the tree.
            self.root = new_contact
        else:
            # Otherwise, call the _insert_helper method to
            # recursively traverse the tree from the root to a leaf node.
            self._insert_helper(self.root, new_contact)

    def _insert_helper(self, current, new_contact):
        """
        A helper method for the insert method that recursively
        traverses the binary search tree to find the correct
        position to insert a new Contact object.
        """
        if new_contact.name == current.name:
            # If the name of the new Contact object matches the name
            # of the current node, replace the phone number of the
            # current node with the phone number of the new Contact object.
            current.phone = new_contact.phone

        elif new_contact.name < current.name:
            # If the name of the new Contact object is less
            # than the name of the current node, go left.
            if current.left is None:
                # If the current node does not have a left child,
                # insert the new Contact object as the left child.
                current.left = new_contact
            else:
                # Otherwise, recursively call the _insert_helper method
                # with the left child as the new current node.
                self._insert_helper(current.left, new_contact)

        else:
            # If the name of the new Contact object is greater
            # than the name of the current node, go right.
            if current.right is None:
                # If the current node does not have a right child,
                # insert the new Contact object as the right child.
                current.right = new_contact
            else:
                # Otherwise, recursively call the _insert_helper
                # method with the right child as the new current node.
                self._insert_helper(current.right, new_contact)

    def search(self, name):
        """
        Searches the binary search tree for a Contact object with the specified name.
        Returns True if a Contact object with that name exists in the binary search tree,
        or False otherwise.
        """
        return self._recursive_search(self.root, name)

    def _recursive_search(self, current, name):
        """
        A recursive helper method for the search method that
        traverses the binary search tree to find the Contact object
        with the specified name.
        """
        if current is None:
            # If the method reaches a leaf node without finding a match, return False.
            return False
        elif name == current.name:
            # If the name of the current node matches the specified name, return True.
            return True
        elif name < current.name:
            # If the specified name is less than the name of the current node,
            # recursively call the _recursive_search method with the left child as the new current node.
            return self._recursive_search(current.left, name)
        else:
            # If the specified name is greater than the name of the current node,
            # recursively call the _recursive_search method with the right child as the new current node.
            return self._recursive_search(current.right, name)

    def delete(self, name):
        """
        Calls the recursive delete method to delete a node only if it has no children
        """
        self.root = self._recursive_delete(self.root, name)

    def _recursive_delete(self, current, name):
        """
        A recursive helper method for the delete method
        """

        if current is None:
            return None
        elif name == current.name:
            if current.left is None and current.right is None:
                # If the current node has no children, delete it by returning None.
                return None
            else:
                # Otherwise, return the current node unchanged.
                return current
        elif name < current.name:
            current.left = self._recursive_delete(current.left, name)
        else:
            current.right = self._recursive_delete(current.right, name)
        return current

    def display(self):
        """
        Calls the recursive display method to display all the contact information in order
        """
        if self.root is None:
            print("Contact book is empty.")
        else:
            self._display_helper(self.root)

    def _display_helper(self, current):
        """
        A recursive helper method for the display method
        """
        if current is not None:
            self._display_helper(current.left)
            print(f"Name: {current.name}, Phone: {current.phone}")
            self._display_helper(current.right)

# Create a new contact book
contactBook = ContactBook()

# Add some contacts to your book
contactBook.insert("Dicmary","+58 993219319")
contactBook.insert("Dicsson","+54 913993219")
contactBook.insert("Enma","+54 9112313219")
contactBook.insert("Jhosep","+54 9111231219")
contactBook.insert("Luis","+54 91123123219")

# Display all the contacts in order

contactBook.display()

# Remove a contact to your book

contactBook.delete("Dicmary") # Can't remove because has children

contactBook.delete("Luis") # Should be ok to remove

# Display all the contacts in order

contactBook.display()

```

Congratulations! you have finished your first Binary Search Tree, now you can more efficiently find your contacts, add new ones, update your contact information and delete any contacts that you don't need

![Happy person with an organized contact book](https://i.imgur.com/bFQPBUG.jpg)

## Example Problem

This is our final problem for this tutorial, if you find yourself having some trouble with this problem don't worry, try to read carefully the requirements, follow the hints and remember to not give up! it is a little difficult to visualize the base case on all our functions but this all comes with practice

Lets revisit our previous Music Playlist linked list and let's convert it to a Music Library that uses a binary search tree to organize our music albums.

Each album should have a title, an author, and a number of songs. We need to implement a display function to print all the albums in alphabetical order, an insert function to add new albums to the library, and a delete function to remove albums that have 1 or 0 children. We also need to track the total number of albums in the library and have a method to print out the height of the binary search tree. We will use recursion to implement the required functionality.

hints: remember how we tracked the prices on our linked list problem? it could help you a lot if you re visited your solution.

The formula to calculate the height of a binary search tree looks something like this max(left_height, right_height) + 1

Requirements:

- Implement a Music Library using a binary search tree to organize the albums.

- Each album should have a title, an author, and a number of songs.

- Implement a display function to print all the albums in alphabetical order.

- Implement an insert function to add new albums to the library.

- Implement a delete function to remove albums that have 1 or 0 children.

- Track the total number of albums in the library.

- Implement a method to print out the height of the binary search tree.

- Use recursion to implement the required functionality.

Copy the code below to start working on your solution, compare your solution to [this example solution](python/03_music_library_solution.py).

```python
'''
Let's revisit our previous Music Playlist linked list and lets convert it
to a Music Library that uses a binary search tree to organize our music albums.

Each album should have a title, an author, and a number of songs.
We need to implement a display function to print all the albums in
alphabetical order, an insert function to add new albums to the library,
and a delete function to remove albums that have 1 or 0 children.
We also need to track the total number of albums and songs in the library and have a method
to print out the height of the binary search tree.

We will use recursion to implement the required functionality.
'''

class MusicLibrary:
    class Album:
        def __init__(self, title, author, num_songs):
            #crete a title, author, num songs, left and right attribute
            self.left = None
            self.right = None

    def __init__(self):
        #crete a root, num_albums and total songs attribute
        self.root = None

    def insert(self, title, author, num_songs):
        #insert a new album into the binary search tree
        new_album = self.Album(title, author, num_songs)
        if self.root is None:
            self.root = new_album
        else:
            self._insert_helper(self.root, new_album)

        #remember to update the number of albums and the total number of songs

    def _insert_helper(self, current, new_album):
        #if the album title is the same replace the author and number of songs
        if new_album.title == current.title:
            pass
        #if the new title is lower than the current title and the left pointer is empty insert the song
        # keep going to the left if otherwise
        elif new_album.title < current.title:
            if current.left is None:
                pass
            else:
                pass
        #if the new title is higher than the current title and the right pointer is empty insert the song
        # keep going to the right if otherwise
        else:
            if current.right is None:
                pass
            else:
                pass

    def delete(self, title):
        #deletes any node that has 0 children or only 1 children, remember to replace the
        #deleted node with their own child to keep the continuity of the tree
        self.root = self._recursive_delete(self.root, title)

    def _recursive_delete(self, current, title):
        if current is None:
            return None
        elif title == current.title:
            if current.left is None and current.right is None:
                # If the current node has no children, delete it by returning None.
                # and update the number of albums and songs
                pass
            elif current.left is None:
                # If the current node has only a right child, replace it with its right child.
                # and update the number of albums and songs
                pass
            elif current.right is None:
                # If the current node has only a left child, replace it with its left child.
                # and update the number of albums and songs
                pass
            else:
                # If the current node has two children we can't delete this node
                print("This node can't be deleted because it has two children")

        elif title < current.title:
            #keep searching to the left if the title is lower than the current title
            current.left = self._recursive_delete(current.left, title)
        else:
            #keep searching to the right if the title is higher than the current title
            current.right = self._recursive_delete(current.right, title)
        return current

    def display(self):
        # Display the total number of albums, total number of songs and each album title
        # author and corresponding number of songs
        if self.root is None:
            print("Music library is empty.")
        else:
            print(f"Total albums: {self.num_albums}, Total songs: {self.total_songs}")
            self._display_helper(self.root)


    def _display_helper(self, current):
        # Traverse trough the binary search tree to display each album in order. the left
        # branches first and the right branches after

        if current is not None:
            pass

    def height(self):
        # Return the height of the binary search tree, remember that re formula is
        # max(left_height, right_height) + 1

        return self._height_helper(self.root)

    def _height_helper(self, current):
        # You might find this easier to understand if you  study the previous recursion problems
        # explained on the tutorial
        if current is None:
            return 0
        else:
            #fill code here to store the heigh of the left brach

            # fill code here to store the heigh of the right branch

            return #use the formula to calculate the height

# Create a new music library and insert some albums
my_library = MusicLibrary()
my_library.insert("The Dark Side of the Moon", "Pink Floyd", 10)
my_library.insert("Thriller", "Michael Jackson", 9)
my_library.insert("Abbey Road", "The Beatles", 17)

# Display the contents of the music library
my_library.display()
print("\n======================")
# Expected output:
# Total albums: 3, Total songs: 36
# Title: Abbey Road, Author: The Beatles, Number of Songs: 17
# Title: The Dark Side of the Moon, Author: Pink Floyd, Number of Songs: 10
# Title: Thriller, Author: Michael Jackson, Number of Songs: 9

# Delete an album that has no children
my_library.delete("Thriller")
my_library.display()
print("\n======================")
# Expected output:
# Total albums: 2, Total songs: 27
# Title: Abbey Road, Author: The Beatles, Number of Songs: 17
# Title: The Dark Side of the Moon, Author: Pink Floyd, Number of Songs: 10

# Delete an album that has one child
my_library.delete("Abbey Road")
my_library.display()
print("\n======================")
# Expected output:
# Total albums: 1, Total songs: 10
# Title: The Dark Side of the Moon, Author: Pink Floyd, Number of Songs: 10

# Try to delete an album that has two children
my_library.insert("The Wall", "Pink Floyd", 26)
my_library.delete("The Dark Side of the Moon")
# Expected output:
# This node can't be deleted because it has two children

# Calculate the height of the binary search tree
print(f"height: {my_library.height()}")
print("\n======================")
# Expected output: 1
```
