import string

from find_boxes import load_boxes_ids


def checksum():
    """Return checksum value as product of all unique IDs with
    2 (two) and/or 3 (three) common letters."""
    boxes = load_boxes_ids()
    two_letters = []
    three_letters = []
    chars = string.ascii_lowercase

    for box in boxes:
        for char in chars:
            count = box.count(char)
            if count == 3 and box not in three_letters:
                three_letters.append(box)
            elif count == 2 and box not in two_letters:
                two_letters.append(box)

    print(f"Checksum value: {len(three_letters) * len(two_letters)}")


if __name__ == "__main__":
    checksum()
