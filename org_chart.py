from printerqueue import Queue

class Node():
    """Node in a tree."""

    def __init__(self, data, children):
        self.data = data
        self.children = children

    def __repr__(self):
        """Reader-friendly representation."""

        return f"<Node {self.data}>"

    def find(self, data):
        """Return node object with this data.

        Start here. Return None if not found.
        """

        to_visit = [self]

        while to_visit:
            current = to_visit.pop()

            if current.data == data:
                return current

            to_visit.extend(current.children)


class Tree():
    """Tree."""

    def __init__(self, root):
        self.root = root

    def __repr__(self):
        """Reader-friendly representation."""

        return f"<Tree root={self.root}>"

    def find_in_tree(self, data):
        """Return node object with this data.

        Start at root.
        Return None if not found.
        """

        return self.root.find(data)
    
    def node_count(self):
        q = Queue(self)
        counter = 0
        while q:
            for i in q:
                counter+=1
                q.dequeue(i)

        return counter




def make_tree(ceo_name, direct_reports):
    child = Node(direct_reports, None)
    root = Node(ceo_name, direct_reports)
    tree = Tree(root)
    return tree

tree = make_tree("Bobby", ['Joe',"Mary", 'Sue'])

print(tree.find_in_tree("Sue"))

# print(tree.node_count())