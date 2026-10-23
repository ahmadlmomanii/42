def input_temperature(temp_str: str) -> int:
    temp: int = int(temp_str)
    return temp


def test_temperature(temp: str) -> None:
    print(f"Input data is '{temp}'")
    try:
        result = input_temperature(temp)
        print(f"Temperature is now {result}°C")
    except Exception as error:
        print(f"Caught input_temperature error: {error}")


def main() -> None:
    print("=== Garden Temperature ===")
    test_temperature("25")
    test_temperature("abc")
    print("All tests completed - program didn’t crash!")


if __name__ == "__main__":
    main()
