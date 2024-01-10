#!/usr/bin/python3
"""
Solution to the Lockboxes problem:
    You have n number of locked boxes in front of you. Each box is numbered
    sequentially from 0 to n - 1 and each box may contain keys to the other
    boxes.
"""


def canUnlockAll(boxes):
    """
    Determines if all box in boxes can be opened

    Return: True if all boxes can be opened, else return False
    """
    boxesNotVisited = []
    boxStates = {}
    traversed = 0

    for i in range(len(boxes)):
        boxesNotVisited.append(i)
        if i == 0:
            boxStates['0'] = True
            continue
        boxStates[str(i)] = False
    # print('BoxesNotVisited are {}'.format(boxesNotVisited))
    # print('BoxStates are {}'.format(boxStates))

    while (len(boxesNotVisited) > 0 and traversed < (len(boxes) ** 2)):
        for i in range(len(boxes)):
            # print('Found box {}'.format(i))
            if i in boxesNotVisited and boxStates[str(i)]:
                for key in boxes[i]:
                    # print('Unlocking box {}'.format(key))
                    if key < len(boxes) and not boxStates[str(key)]:
                        boxStates[str(key)] = True
                # print('Boxstates: {}'.format(boxStates))
                boxesNotVisited.remove(i)
                # print('Uexplored boxes are {}'.format(boxesNotVisited))
            if False not in boxStates.values():
                return True
            traversed += 1

    return False not in boxStates.values()
