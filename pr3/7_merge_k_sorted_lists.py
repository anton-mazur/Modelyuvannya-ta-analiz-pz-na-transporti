import heapq

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

def merge_k_lists(lists):
    heap = []
    for i, head in enumerate(lists):
        if head:
            heapq.heappush(heap, (head.val, i, head))

    dummy = ListNode(0)
    curr = dummy
    counter = len(lists)

    while heap:
        val, idx, node = heapq.heappop(heap)
        curr.next = node
        curr = curr.next
        if node.next:
            counter += 1
            heapq.heappush(heap, (node.next.val, counter, node.next))

    return dummy.next

if __name__ == "__main__":
    # Тест 1
    l1 = build_list([1, 4, 5])
    l2 = build_list([1, 3, 4])
    l3 = build_list([2, 6])
    res1 = merge_k_lists([l1, l2, l3])
    print("Приклад 1:", to_list(res1))  # [1, 1, 2, 3, 4, 4, 5, 6]

    # Тест 2
    res2 = merge_k_lists([])
    print("Приклад 2:", to_list(res2))  # []

    # Тест 3
    res3 = merge_k_lists([build_list([])])
    print("Приклад 3:", to_list(res3))  # []
