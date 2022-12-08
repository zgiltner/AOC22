import numpy as np


def create_array():
    array = np.empty([len(data), len(data[0])])
    for j, item in enumerate(data):
        for i, number in enumerate(item):
            n = int(number)
            array[j, i] = n
    return array


def get_all_values(array, i, j):
    values_bottom = []
    values_top = []
    values_left = []
    values_right = []
    for m in range(i+1, array.shape[0]):
        values_bottom.append(array[m, j])
    for m in range(0, i):
        values_top.append(array[m, j])
    for n in range(0, j):
        values_left.append(array[i, n])
    for n in range(j+1, array.shape[1]):
        values_right.append(array[i, n])
    values_top.reverse()
    values_left.reverse()
    return values_bottom, values_top, values_left, values_right


def calculate_row_visibility(array, row, i, j):
    score = 0
    current_value = array[i, j]
    for t in row:
        score += 1
        if t >= current_value:
            break
    return score


def calculate_tree_score(array, rows, i, j):
    tree_score = 1
    for row in rows:
        val = calculate_row_visibility(array, row, i, j)
        tree_score *= val
    return tree_score


def calculate_visible_trees(four_sides, max_height):
    score = 0
    for row_trees in four_sides:
        visible = True
        for t in row_trees:
            if t >= max_height:
                visible = False
                break
        if visible:
            score += 1
            break
    return score


if __name__ == "__main__":
    with open("d8input.txt", "r") as f:
        data = f.read().splitlines()
    print(data)
    trees = create_array()
    print(trees)

    max_score = 0
    # edges
    visible_trees = trees.shape[0]*2 + trees.shape[1] * 2 - 4
    # inside
    a, b = trees.shape
    for i in range(1, a-1):
        for j in range(1, b-1):
            current_value = trees[i, j]
            directions = get_all_values(trees, i, j)
            visible_trees += calculate_visible_trees(directions, current_value)
            score = calculate_tree_score(trees, directions, i, j)
            if score > max_score:
                max_score = score

    print(visible_trees)
    print(max_score)
