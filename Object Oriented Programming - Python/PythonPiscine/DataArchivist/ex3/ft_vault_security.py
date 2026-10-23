def secure_archive(
        name: str, action: str = "r", content: str = ""
        ) -> tuple[bool, str]:
    try:
        if action == "r":
            with open(name, "r") as f:
                return (True, f.read())
        elif action == "w":
            with open(name, "w") as f:
                f.write(content)
                return (True, "Content successfully written to file")
        return (False, "Invalid action")
    except Exception as e:
        return (False, str(e))


def main() -> None:
    print("=== Cyber Archives Security ===")
    print("\nUsing ’secure_archive’ to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))
    print("\nUsing ’secure_archive’ to read from an inaccessible file:")
    print(secure_archive("/etc/shadow"))
    print("\nUsing ’secure_archive’ to read from a regular file:")
    res = secure_archive("archive.txt")
    print(res)
    print("\nUsing ’secure_archive’ to write previous content to a new file:")
    if res[0]:
        print(secure_archive("to_write_in.txt", "w", res[1]))
    else:
        print(res)


if __name__ == "__main__":
    main()
