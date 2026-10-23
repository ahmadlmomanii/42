import sys


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{sys.argv[1]}'")
    file = None
    try:
        file = open(sys.argv[1], "r")
        content = file.read()
        print("---\n")
        print(content)
        print("---")
    except Exception as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
    finally:
        if file is not None:
            file.close()
            print(f"File '{sys.argv[1]}' closed.")


if __name__ == "__main__":
    main()
