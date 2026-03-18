from LinkedList import LinkedList, Node

# Setup
ll = LinkedList()

song_a = Node(name="Blinding Lights", artist="The Weeknd", album="After Hours")
song_b = Node(name="Bohemian Rhapsody", artist="Queen", album="A Night at the Opera")
song_c = Node(name="Stairway to Heaven", artist="Led Zeppelin", album="Led Zeppelin IV")

ll.insert_at_beginning(song_a)
ll.insert_at_beginning(song_b)
ll.insert_at_beginning(song_c)
print(ll)

# Test insert_at_end
print("\nTest insert_at_end:")
song_d = Node(name="Hotel California", artist="Eagles", album="Hotel California")
ll.insert_at_end(song_d)
print(ll)

# Test insert_after_node
print("\nTest insert_after_node:")
song_x = Node(name="Smells Like Teen Spirit", artist="Nirvana", album="Nevermind")
ll.insert_after_node(song_x, "Bohemian Rhapsody")
print(ll)

# Test search
print("\nTest search:")
result = ll.search("Smells Like Teen Spirit")
print(f'Search Smells Like Teen Spirit: {result.song_data["name"] if result else "Not found"}')
result = ll.search("Imagine")
print(f'Search Imagine: {result.song_data["name"] if result else "Not found"}')

# Test delete_node
print("\nTest delete_node:")
ll.delete_node("Smells Like Teen Spirit")
print(f"After deleting Smells Like Teen Spirit: {ll}")
ll.delete_node("Stairway to Heaven")
print(f"After deleting Stairway to Heaven (head): {ll}")
ll.delete_node("Hotel California")
print(f"After deleting Hotel California (tail): {ll}")