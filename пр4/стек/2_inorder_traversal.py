from __future__ import annotations

from dataclasses import dataclass


@dataclass
class TreeNode:
    val: int = 0
    left: TreeNode | None = None
    right: TreeNode | None = None


def inorder_traversal(root: TreeNode | None) -> list[int]:
    result: list[int] = []
    stack: list[TreeNode] = []
    current = root

    while current is not None or stack:
        while current is not None:
            stack.append(current)
            current = current.left

        current = stack.pop()
        result.append(current.val)
        current = current.right

    return result


if __name__ == "__main__":
    root = TreeNode(1, right=TreeNode(2, left=TreeNode(3)))
    print(inorder_traversal(root))
