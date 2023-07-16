"""
    Let's say you start looking at your contacts on your note book and start searching for the new number of your best friend, but
    you have so many contacts in your note book that it takes you way too much time to go trough the contacts one by one,
    your task it to create a fast and efficient way to organize your contacts in python to make it easier for you to find everything.
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