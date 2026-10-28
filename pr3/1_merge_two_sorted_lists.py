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

def merge_two_lists(list1, list2):
    dummy = ListNode(0)
    tail = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    tail.next = list1 if list1 else list2
    return dummy.next

if __name__ == "__main__":
    # Тест 1
    l1 = build_list([1, 2, 4])
    l2 = build_list([1, 3, 4])
    res1 = merge_two_lists(l1, l2)
    print("Приклад 1:", to_list(res1))  # [1, 1, 2, 3, 4, 4]

    # Тест 2
    l1 = build_list([])
    l2 = build_list([])
    res2 = merge_two_lists(l1, l2)
    print("Приклад 2:", to_list(res2))  # []

    # Тест 3
    l1 = build_list([])
    l2 = build_list([0])
    res3 = merge_two_lists(l1, l2)
    print("Приклад 3:", to_list(res3))  # [0]
