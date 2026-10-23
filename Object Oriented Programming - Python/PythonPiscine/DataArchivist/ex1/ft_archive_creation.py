import sys
from typing import IO


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{sys.argv[1]}'")
    file: IO[str] | None = None
    na: IO[str] | None = None
    try:
        file = open(sys.argv[1], "r")
        content: str = file.read()
        print("---\n")
        print(content)
        print("---")
        print(f"File '{sys.argv[1]}' closed.")
        print("\nTransform data:")
        print("---\n")
        new: list[list[str]] = []
        tmp: list[str] = []
        i = 0
        while (i < len(content)):
            tmp = []
            while (i < len(content) and content[i] != "\n"):
                tmp.append(content[i])
                i += 1
            tmp.append("#")
            new.append(tmp)
            i += 1
        i = 0
        while (i < len(new)):
            print("".join(new[i]))
            i += 1
        na_file = input("\n---\nEnter new file name (or empty):")
        if na_file:
            na = open(na_file, "w")
            i = 0
            for i in range(len(new)):
                na.write("".join(new[i]))
                na.write("\n")
            print(f"Saving data to ’{na_file}’")
            print(f"Data saved in file ’{na_file}’.")
        else:
            print("Not saving data.")
    except Exception as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
    finally:
        if file is not None:
            file.close()
        if na is not None:
            na.close()


if __name__ == "__main__":
    main()
