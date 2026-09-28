class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swap_pairs(head):
    if head is None or head.next is None:
        return head

    first = head
    second = head.next
    first.next = swap_pairs(second.next)
    second.next = first
    return second

def build(values):
    if not values:
        return None
    return ListNode(values[0], build(values[1:]))


def to_list(head):
    if head is None:
        return []
    return [head.val] + to_list(head.next)


print(to_list(swap_pairs(build([1, 2, 3, 4]))))  # [2, 1, 4, 3]
print(to_list(swap_pairs(build([]))))            # []
print(to_list(swap_pairs(build([1]))))           # [1]
print(to_list(swap_pairs(build([1, 2, 3]))))     # [2, 1, 3]