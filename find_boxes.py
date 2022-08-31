from itertools import combinations


def load_boxes_ids() -> list:
    """Load all IDs from txt file and return as list."""
    with open("input.txt", "r") as f:
        boxes = f.read().split("\n")
        f.close()
    return boxes


def find_boxes():
    """Find correct boxes IDs (one letter diff):
    Build all possible combinations of 2 (two) IDs and compare them.
    Select combination with one diff and print results.
    """
    boxes = load_boxes_ids()
    combos = combinations(boxes, 2)

    for combo in combos:
        i = 0
        diff = 0
        a = combo[0]
        b = combo[1]

        while diff <= 1 and i < len(a):
            if a[i] != b[i]:
                diff += 1
            i += 1

        if diff == 1 and i == len(a):
            common_letters = ""

            for i in range(len(a)):
                if a[i] == b[i]:
                    common_letters += a[i]
                else:
                    diff = i

            print(f"Correct box IDs: '{a}' and '{b}'")
            print(f"Common letters: '{common_letters}'")
            print(f"Diff: {a[diff]} and {b[diff]} at index {diff}")

            break


if __name__ == "__main__":
    find_boxes()
