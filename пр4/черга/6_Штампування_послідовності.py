def moves_to_stamp(stamp: str, target: str) -> list[int]:
    target_list = list(target)
    n, m = len(target), len(stamp)
    used = [False] * (n - m + 1)
    result = []
    replaced = 0

    def replace_at(start: int) -> int:
        changed = 0
        for offset in range(m):
            if target_list[start + offset] != "?":
                target_list[start + offset] = "?"
                changed += 1
        return changed

    while replaced < n:
        progress = False
        for start in range(n - m + 1):
            if used[start]:
                continue
            matches = True
            has_new_character = False
            for offset in range(m):
                current = target_list[start + offset]
                if current != "?" and current != stamp[offset]:
                    matches = False
                    break
                if current != "?":
                    has_new_character = True
            if matches and has_new_character:
                used[start] = True
                replaced += replace_at(start)
                result.append(start)
                progress = True
        if not progress:
            return []

    result.reverse()
    return result
