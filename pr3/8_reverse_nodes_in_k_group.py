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

def reverse_k_group(head, k):
    if not head or k <= 1:
        return head

    curr = head
    count = 0
    while curr and count < k:
        curr = curr.next
        count += 1

    if count == k:
        prev = reverse_k_group(curr, k)
        curr = head
        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        head = prev

    return head

if __name__ == "__main__":
    # Тест 1
    h1 = build_list([1, 2, 3, 4, 5])
    res1 = reverse_k_group(h1, 2)
    print("Приклад 1:", to_list(res1))  # [2, 1, 4, 3, 5]

    # Тест 2
    h2 = build_list([1, 2, 3, 4, 5])
    res2 = reverse_k_group(h2, 3)
    print("Приклад 2:", to_list(res2))  # [3, 2, 1, 4, 5]
