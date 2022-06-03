class Node():
    def __init__(self, val, children: list['Node'] = []) -> None:
        self.val = val
        self.children = children


#           1
#        /     \
#       2        3
#     /   \    /   \
#    4     5  6     7

four = Node(4)
five = Node(5)
six = Node(6)
seven = Node(7)

two = Node(2, [four, five])
three = Node(3, [six, seven])

one = Node(1, [two, three])

basicTree = one
