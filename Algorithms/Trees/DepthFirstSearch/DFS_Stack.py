from BasicTree import basicTree, Node


def dfs(root: 'Node') -> None:
    stack = [root]

    while len(stack) > 0:
        top = stack.pop(-1)

        print(f'{top.val}')

        for child in top.children:
            stack.append(child)

dfs(basicTree)