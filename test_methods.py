from LinkedList import LinkedList, Node

# Setup
ll = LinkedList()
node_a = Node('A')
node_b = Node('B')
node_c = Node('C')

ll.insert_at_beginning(node_a)
ll.insert_at_beginning(node_b)
ll.insert_at_beginning(node_c)
print(ll)

# Test insert_at_end
print('\nTest insert_at_end:')
node_d = Node('D')
ll.insert_at_end(node_d)
print(ll)

# Test insert_after_node
print('\nTest insert_after_node:')
node_x = Node('X')
ll.insert_after_node(node_x, 'B')
print(ll)

# Test search
print('\nTest search:')
result = ll.search('X')
print(f'Search X: {result.data if result else "Not found"}')
result = ll.search('Z')
print(f'Search Z: {result.data if result else "Not found"}')

# Test delete_node
print('\nTest delete_node:')
ll.delete_node('X')
print(f'After deleting X: {ll}')
ll.delete_node('C')
print(f'After deleting C (head): {ll}')
ll.delete_node('D')
print(f'After deleting D (tail): {ll}')