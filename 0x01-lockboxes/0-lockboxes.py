#!/usr/bin/python3
"""
Definition of 'canUnlockAll' which accepts a list of lists argument
representing boxes an the number(s) in them, keys to boxes they unlock
"""


def updateKeys(allKeys, boxes, box, checked, index):
    """
    Recursively loops through boxes and the boxes which key are contained  in
    them to gather all possible keys
    """

    for key in box:
        if len(checked) == 0:
            checked.add(0)
        if key not in allKeys:
            allKeys.add(key)
        if key >= len(boxes):
            return
        if key not in checked:
            checked.add(index)
            updateKeys(allKeys, boxes, boxes[key], checked, index=key)


def canUnlockAll(boxes):
    """
    Check the keys in all the boxes and checks whether or not they can be
    opened

    Return: True if all boxes can be opened, else return False
    """
    if len(boxes) <= 1:
        return True
    keys = set()
    checked = set()
    updateKeys(keys, boxes, boxes[0], checked, 0)
    keys.add(0)
    for i in range(len(boxes)):
        if i not in keys:
            return False
    return True
