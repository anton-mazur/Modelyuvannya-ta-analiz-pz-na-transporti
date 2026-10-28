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

def partition(head, x):
    before_dummy = ListNode(0)
    after_dummy = ListNode(0)

    before = before_dummy
    after = after_dummy

    curr = head
    while curr:
        if curr.val < x:
            before.next = curr
            before = before.next
        else:
            after.next = curr
            after = after.next
        curr = curr.next

    after.next = None
    before.next = after_dummy.next

    return before_dummy.next

if __name__ == "__main__":
    # Тест 1
    h1 = build_list([1, 4, 3, 2, 5, 2])
    res1 = partition(h1, 3)
    print("Приклад 1:", to_list(res1))  # [1, 2, 2, 4, 3, 5]

    # Тест 2
    h2 = build_list([2, 1])
    res2 = partition(h2, 2)
    print("Приклад 2:", to_list(res2))  # [1, 2]
