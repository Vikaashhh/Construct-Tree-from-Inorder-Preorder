class Node:
    def __init__(self, data):  # Node structure
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder, preorder):
        # Dictionary to store inorder value -> index mapping
        inorder_index_map = {value: idx for idx, value in enumerate(inorder)}
        
        # Preorder ka index track karne ke liye ek pointer
        self.pre_idx = 0

        # Helper function to construct tree recursively
        def construct(in_start, in_end):
            # Agar invalid range ho toh None return karo
            if in_start > in_end:
                return None

            # preorder ka current element root hoga
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = Node(root_val)

            # Agar root ka koi child nahi h (leaf node)
            if in_start == in_end:
                return root

            # root ki position inorder mein find karo
            in_index = inorder_index_map[root_val]

            # Left and right subtree ko build karo
            root.left = construct(in_start, in_index - 1)
            root.right = construct(in_index + 1, in_end)

            return root

        return construct(0, len(inorder) - 1)
