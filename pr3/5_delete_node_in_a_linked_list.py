class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_list(values):
    dummy = ListNode(0)
    curr = dummy
    for val in values:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def to_list(head):
    res = []
    curr = head
    while curr:
        res.append(curr.val)
        curr = curr.next
    return res

def find_node(head, val):
    curr = head
    while curr:
        if curr.val == val:
            return curr
        curr = curr.next
    return None

def delete_node(node):
    node.val = node.next.val
    node.next = node.next.next

if __name__ == "__main__":
    # Тест 1
    h1 = build_list([4, 5, 1, 9])
    node_to_del1 = find_node(h1, 5)
    delete_node(node_to_del1)
    print("Приклад 1:", to_list(h1))  # [4, 1, 9]

    # Тест 2
    h2 = build_list([4, 5, 1, 9])
    node_to_del2 = find_node(h2, 1)
    delete_node(node_to_del2)
    print("Приклад 2:", to_list(h2))  # [4, 5, 9]
