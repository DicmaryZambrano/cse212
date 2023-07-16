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
            self.title = title
            self.author = author
            self.num_songs = num_songs
            self.left = None
            self.right = None

    def __init__(self):
        #crete a root, num_albums and total songs attribute
        self.root = None
        self.num_albums = 0
        self.total_songs = 0

    def insert(self, title, author, num_songs):
        #insert a new album into the binary search tree
        new_album = self.Album(title, author, num_songs)
        if self.root is None:
            self.root = new_album
        else:
            self._insert_helper(self.root, new_album)

        #remember to update the number of albums and the total number of songs
        self.num_albums += 1
        self.total_songs += num_songs

    def _insert_helper(self, current, new_album):
        #if the album title is the same replace the author and number of songs
        if new_album.title == current.title:
            current.author = new_album.author
            current.num_songs = new_album.num_songs
        #if the new title is lower than the current title and the left pointer is empty insert the song
        # keep going to the left if otherwise 
        elif new_album.title < current.title:
            if current.left is None:
                current.left = new_album
            else:
                self._insert_helper(current.left, new_album)
        #if the new title is higher than the current title and the right pointer is empty insert the song
        # keep going to the right if otherwise 
        else:
            if current.right is None:
                current.right = new_album
            else:
                self._insert_helper(current.right, new_album)

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
                self.num_albums -= 1
                self.total_songs -= current.num_songs
                return None
            elif current.left is None:
                # If the current node has only a right child, replace it with its right child.
                self.num_albums -= 1
                self.total_songs -= current.num_songs
                return current.right
            elif current.right is None:
                # If the current node has only a left child, replace it with its left child.
                self.num_albums -= 1
                self.total_songs -= current.num_songs
                return current.left
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
            self._display_helper(current.left)
            print(f"Title: {current.title}, Author: {current.author}, Number of Songs: {current.num_songs}")
            self._display_helper(current.right)

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
            left_height = self._height_helper(current.left) #fill code here to store the heigh of the left brach
            right_height = self._height_helper(current.right) # fill code here to store the heigh of the right branch
            return max(left_height, right_height) + 1 #use the formula to calculate the height