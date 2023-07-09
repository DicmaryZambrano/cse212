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
                return

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