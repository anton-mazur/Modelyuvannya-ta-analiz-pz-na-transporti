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

def delete_duplicates(head):
    curr = head
    while curr and curr.next:
        if curr.val == curr.next.val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head

if __name__ == "__main__":
    # Тест 1
    h1 = build_list([1, 1, 2])
    res1 = delete_duplicates(h1)
    print("Приклад 1:", to_list(res1))  # [1, 2]

    # Тест 2
    h2 = build_list([1, 1, 2, 3, 3])
    res2 = delete_duplicates(h2)
    print("Приклад 2:", to_list(res2))  # [1, 2, 3]
