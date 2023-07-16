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