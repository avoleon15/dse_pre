class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        return f"(DATA: {self.data} | NEXT: {self.next})"


class LinkedList:
    def __init__(self):
        self.start = None

    def __repr__(self) -> str:
        nodes = ['START']
        for node in self:
            nodes.append(node.data)
        nodes.append('NIL')
        return '\n' + ' --> '.join(nodes)

    def __iter__(self):
        node = self.start
        while node is not None:
            yield node
            node = node.next

    def __len__(self) -> int:
        length = 0
        for _ in self:
            length += 1
        return length

    def traverse(self) -> None:
        for node in self:
            print(node.data)

    def insert_at_beginning(self, element: Node) -> None:
        element.next = self.start
        self.start = element

    def insert_at_end(self, element: Node) -> None:
        node = self.start
        if self.start is None:
            self.start = element
            return
        
        while node.next is not None:
            node = node.next
        node.next = element

    def insert_after_node(self, element: Node, node_reference) -> None:
        node = self.start
        while node is not None:
            if node.data == node_reference:
                element.next = node.next
                node.next = element
                return
            node = node.next

    def delete_node(self, element_data) -> None:
        node = self.start
        if self.start is None:
            return

        if self.start.data == element_data:
            self.start = self.start.next
            return

        while node.next is not None:
            if node.next.data == element_data:
                node.next = node.next.next
                return
            node = node.next
            
    def search(self, element_data) -> "Node | None":
        for node in self:
            if node.data == element_data:
                return node
        return None