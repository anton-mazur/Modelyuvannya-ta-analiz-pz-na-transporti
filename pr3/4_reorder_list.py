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

def reorder_list(head):
    if not head or not head.next:
        return head

    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    prev = None
    curr = slow.next
    slow.next = None  

    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    first = head
    second = prev
    while second:
        tmp1 = first.next
        tmp2 = second.next

        first.next = second
        second.next = tmp1

        first = tmp1
        second = tmp2

    return head

if __name__ == "__main__":
    # Тест 1
    h1 = build_list([1, 2, 3, 4])
    reorder_list(h1)
    print("Приклад 1:", to_list(h1))  # [1, 4, 2, 3]

    # Тест 2
    h2 = build_list([1, 2, 3, 4, 5])
    reorder_list(h2)
    print("Приклад 2:", to_list(h2))  # [1, 5, 2, 4, 3]
