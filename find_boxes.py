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
        while diff <= 1 and i < len(combo[0]):
            if combo[0][i] != combo[1][i]:
                diff += 1
            i += 1

        if diff == 1 and i == len(combo[0]):
            common_letters = ""

            for i in range(len(combo[0])):
                if combo[0][i] == combo[1][i]:
                    common_letters += combo[0][i]

            print(f"Correct box ids: '{combo[0]}' and '{combo[1]}'")
            print(f"Common letters: '{common_letters}'")

            break


if __name__ == "__main__":
    find_boxes()
