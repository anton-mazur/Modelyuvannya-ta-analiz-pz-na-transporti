class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_list_with_cycle(values, pos):
    if not values:
        return None
    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos != -1:
        nodes[-1].next = nodes[pos]
    return nodes[0]

def has_cycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

if __name__ == "__main__":
    # Тест 1
    h1 = build_list_with_cycle([3, 2, 0, -4], 1)
    print("Приклад 1:", has_cycle(h1))  # True

    # Тест 2
    h2 = build_list_with_cycle([1, 2], 0)
    print("Приклад 2:", has_cycle(h2))  # True

    # Тест 3
    h3 = build_list_with_cycle([1], -1)
    print("Приклад 3:", has_cycle(h3))  # False
