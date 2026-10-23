def input_temperature(temp_str: str) -> int:
    temp: int = int(temp_str)
    if temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    elif temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    return temp


def test_temperature(temp: str) -> None:
    print(f"Input data is '{temp}'")
    try:
        result = input_temperature(temp)
        print(f"Temperature is now {result}°C")
    except Exception as error:
        print(f"Caught input_temperature error: {error}")


def main() -> None:
    print("=== Garden Temperature Checker ===")
    print()
    test_temperature("25")
    print()
    test_temperature("abc")
    print()
    test_temperature("100")
    print()
    test_temperature("-50")
    print()
    print("All tests completed - program didn’t crash!")


if __name__ == "__main__":
    main()
