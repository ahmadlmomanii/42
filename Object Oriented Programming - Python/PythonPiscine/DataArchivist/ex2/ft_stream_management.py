import sys
from typing import IO


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_stream_management.py <file>")
        return
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{sys.argv[1]}'")
    file: IO[str] | None = None
    na: IO[str] | None = None
    na_file: str = sys.argv[1]
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
        sys.stdout.write("\n---\nEnter new file name (or empty): ")
        na_file = sys.stdin.readline().rstrip()
    except Exception as e:
        sys.stderr.write(f"[STDERR] Error opening file '{na_file}': {e}\n")
        return
    finally:
        if file is not None:
            file.close()
    if na_file:
        print(f"Saving data to ’{na_file}’")
        try:
            na = open(na_file, "w")
            for i in range(len(new)):
                na.write("".join(new[i]))
                na.write("\n")
            print(f"Data saved in file ’{na_file}’.")
        except Exception as e:
            sys.stderr.write(f"[STDERR] Error opening file '{na_file}': {e}\n")
            sys.stderr.write("Data not saved.\n")
        finally:
            if na is not None:
                na.close()
    else:
        print("Not saving data.")


if __name__ == "__main__":
    main()
