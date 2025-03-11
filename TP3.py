# Construct adjacent matrix for graph G
# Write Inorder algo to exploit tree G which obey behavior:
#   Input node lable (x)
#   Print out all node of subtree (x) in (Inorder)

graph_G = [
    [0, 1, 1, 0, 0, 0, 0, 0], # (1,2) (1,3)
    [0, 0, 0, 0, 1, 1, 0, 0], # (2,5) (2,6)
    [0, 0, 0, 1, 0, 0, 0, 0], # (3,4)
    [0, 0, 0, 0, 0, 0, 0, 1], # (4,8)
    [0, 0, 0, 0, 0, 0, 1, 0], # (5,7)
    [0, 0, 0, 0, 0, 0, 0, 0], # 0
    [0, 0, 0, 0, 0, 0, 0, 0], # 0
    [0, 0, 0, 0, 0, 0, 0, 0], # 0
]

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_tree_from_adjacency_matrix(adj_matrix):
    nodes = [Node(i) for i in range(len(adj_matrix))]

    for i in range(len(adj_matrix)):
        children = [j for j, val in enumerate(adj_matrix[i]) if val == 1]
        if len(children) > 2:
            raise ValueError("Each node can have at most 2 children in a binary tree.")
        if len(children) >= 1:
            nodes[i].left = nodes[children[0]]
        if len(children) == 2:
            nodes[i].right = nodes[children[1]]

    return nodes


def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value + 1, end=' ')
        inorder_traversal(root.right)

if __name__ == "__main__":
    nodes = build_tree_from_adjacency_matrix(graph_G)

    label_of_chosen_root = 2
    print("Inorder traversal of the subtree where label of chosen root is: {}".format(label_of_chosen_root))
    inorder_traversal(nodes[label_of_chosen_root - 1])
    print()