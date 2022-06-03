
from BasicTree import basicTree, Node

def dfs_prefix(node: Node):
    print(f'{node.val} ')

    children = node.children
    for child in children:
        dfs_prefix(child)

dfs_prefix(basicTree)