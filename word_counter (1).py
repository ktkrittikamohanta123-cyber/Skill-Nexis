"""Word Counter from Text File
Counts words, lines and characters.
Topics: file reading, list, tuple, set, dict, exception handling.
"""
import sys
from collections import Counter


def analyze(path):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    lines = text.splitlines()          # list of lines
    words = text.split()               # list of words
    stats = {                          # dictionary of results
        "lines": len(lines),
        "words": len(words),
        "characters (with spaces)": len(text),
        "characters (no spaces)": len("".join(text.split())),
    }
    cleaned = [w.strip(".,;:!?\"'()[]").lower() for w in words]
    cleaned = [w for w in cleaned if w]
    unique_words = set(cleaned)        # set of unique words
    top5 = Counter(cleaned).most_common(5)  # list of (word, count) tuples
    return stats, unique_words, top5


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else input("Enter text file path: ").strip()
    try:
        stats, unique_words, top5 = analyze(path)
    except FileNotFoundError:
        print(f"Error: '{path}' not found.")
        return
    except PermissionError:
        print(f"Error: no permission to read '{path}'.")
        return
    except UnicodeDecodeError:
        print("Error: file is not valid UTF-8 text.")
        return

    print(f"\nResults for {path}")
    print("-" * 30)
    for key, value in stats.items():
        print(f"{key:26}: {value}")
    print(f"{'unique words':26}: {len(unique_words)}")
    print("\nTop 5 words:")
    for word, count in top5:
        print(f"  {word:12} {count}")


if __name__ == "__main__":
    main()
