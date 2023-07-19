import itertools
import os

def create_variations(word):
    character_variations = {
        "a": ("a", "A", "@", "*", "4"),
        "b": ("b", "B", "8"),
        "c": ("c", "C", "<", "{"),
        "d": ("d", "D", "|)"),
        "e": ("e", "E", "3", "&"),
        "f": ("f", "F", "|="),
        "g": ("g", "G", "&"),
        "h": ("h", "H", "#"),
        "i": ("i", "I", "1", "!", "|"),
        "j": ("j", "J"),
        "k": ("k", "K", "|<"),
        "l": ("l", "L", "|_"),
        "m": ("m", "M"),
        "n": ("n", "N", "|\\|"),
        "o": ("o", "O", "0", "()", "[]"),
        "p": ("p", "P"),
        "q": ("q", "Q"),
        "r": ("r", "R"),
        "s": ("s", "S", "$", "5"),
        "t": ("t", "T", "7", "+"),
        "u": ("u", "U", "|_|"),
        "v": ("v", "V"),
        "w": ("w", "W", "\\/\\/", "|/\\|"),
        "x": ("x", "X", "><"),
        "y": ("y", "Y"),
        "z": ("z", "Z", "2", "%"),
        # Add other character variations here...
        "0": ("0", "@"),
        "1": ("1", "!", "|", "i", "I"),
        "2": ("2", "%"),
        "3": ("3", "E", "&"),
        "4": ("4", "A", "@"),
        "5": ("5", "$"),
        "6": ("6", "b"),
        "7": ("7", "T"),
        "8": ("8", "&", "B"),
        "9": ("9", "g"),
    }

    variations = []
    for char in word:
        char_lower = char.lower()
        if char_lower in character_variations:
            variations.append(character_variations[char_lower])
        else:
            variations.append((char,))

    all_variations = [''.join(combination) for combination in itertools.product(*variations)]
    return all_variations

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_file_path = os.path.join(current_dir, "in.txt")
    output_file_path = os.path.join(current_dir, "out.txt")

    with open(input_file_path, "r") as input_file:
        words = input_file.read().splitlines()

    with open(output_file_path, "w") as output_file:
        for word in words:
            variations = create_variations(word)
            for variation in variations:
                output_file.write(f"{variation}\n")

    print("Finished")

if __name__ == "__main__":
    main()
