def in_order(tree):
    stack = []
    empty = 0

    while empty == 0:
        if tree != none:
            stack.append(tree)
            tree = tree.left

        else :
            if (len(stack)>0):
                tree = stack.pop()
                print(tree.value)
                tree = tree.right

            else :
                empty = 1
