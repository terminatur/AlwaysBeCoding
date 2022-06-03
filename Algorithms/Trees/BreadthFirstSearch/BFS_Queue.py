from collections import deque
from BasicTree import Node, basicTree


def bfs(root: 'Node') -> None:
    queue = deque()
    queue.append(root)

    while len(queue) > 0:
        top = queue.popleft()

        print(f'{top.val}')

        for child in top.children:
            queue.append(child)

bfs(basicTree)