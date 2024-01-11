#!/usr/bin/python3
'''Modules for lockboxes'''


from collections import deque

def canUnlockAll(boxes):
    n = len(boxes)
    seen_boxes = set([0])
    unseen_boxes = deque(boxes[0])

    while unseen_boxes:
        boxIdx = unseen_boxes.popleft()
        if not (0 <= boxIdx < n):
            continue
        if boxIdx not in seen_boxes:
            unseen_boxes.extend(boxes[boxIdx])
            seen_boxes.add(boxIdx)

    return n == len(seen_boxes)
