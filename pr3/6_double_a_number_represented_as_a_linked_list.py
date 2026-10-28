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

def double_it(head):
    if head.val >= 5:
        head = ListNode(0, head)

    curr = head
    while curr:
        curr.val = (curr.val * 2) % 10
        if curr.next and curr.next.val >= 5:
            curr.val += 1
        curr = curr.next

    return head

if __name__ == "__main__":
    # Тест 1
    h1 = build_list([1, 8, 9])
    res1 = double_it(h1)
    print("Приклад 1:", to_list(res1))  # [3, 7, 8]

    # Тест 2
    h2 = build_list([9, 9, 9])
    res2 = double_it(h2)
    print("Приклад 2:", to_list(res2))  # [1, 9, 9, 8]
