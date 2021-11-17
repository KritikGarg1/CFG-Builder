import sys
import argparse
CLI=argparse.ArgumentParser()
CLI.add_argument(
  "--lista",  # name on the CLI - drop the `--` for positional/required parameters
  nargs="*",  # 0 or more values expected => creates a list
  type=int,
  default=[],  # default if nothing is provided
)
args = CLI.parse_args()
tests=args.lista

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
 
# A utility function to insert
# a new node with the given key
 
 
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root
 
# A utility function to do inorder tree traversal
 
 
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)
 
 
# Driver program to test the above functions
# Let us create the following BST
#    50
#  /     \
# 30     70
#  / \ / \
# 20 40 60 80
 
r = Node(10)
r = insert(r, 6)
r = insert(r, 4)
r = insert(r, 8)
r = insert(r, 14)
r = insert(r, 12)
r = insert(r, 16)
 
# Print inoder traversal of the BST
for x in tests:
    insert(r,x)

inorder(r)