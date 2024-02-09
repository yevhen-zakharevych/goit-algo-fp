import heapq
import uuid


import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def build_heap_tree(heap):
    if not heap:
        return None

    root = Node(heap[0])
    queue = [(root, 0)]

    while queue:
        node, index = queue.pop(0)
        left_index = 2 * index + 1
        right_index = 2 * index + 2

        if left_index < len(heap):
            node.left = Node(heap[left_index])
            queue.append((node.left, left_index))

        if right_index < len(heap):
            node.right = Node(heap[right_index])
            queue.append((node.right, right_index))
    return root


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_heap(heap_root):
    heap = nx.DiGraph()
    pos = {heap_root.id: (0, 0)}
    heap = add_edges(heap, heap_root, pos)

    colors = [node[1]['color'] for node in heap.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in heap.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(heap, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


if __name__ == "__main__":
    nums = [4, 10, 3, 5, 1]
    heapq.heapify(nums)

    heap_root = build_heap_tree(nums)
    draw_heap(heap_root)
