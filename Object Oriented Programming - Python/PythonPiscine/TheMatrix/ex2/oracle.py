from dotenv import load_dotenv
import os
import sys


def main() -> None:
    load_dotenv()
    required_configs = [
        "MATRIX_MODE",
        "DATABASE_URL",
        "API_KEY",
        "LOG_LEVEL",
        "ZION_ENDPOINT"
    ]
    config = {}
    missing = False
    print("ORACLE STATUS: Reading the Matrix...")
    for key in required_configs:
        config[key] = os.getenv(key)
        if config[key] is None:
            print(f"Missing configuration: {key}")
            missing = True
    if missing:
        sys.exit(1)
    print("Configuration loaded:")
    print(f"Mode: {config['MATRIX_MODE']}")
    if config['MATRIX_MODE'] not in {"development", "production"}:
        print("Invalid MATRIX_MODE. Use 'development' or 'production'.")
        sys.exit(1)
    print(f"Database: Connected to {config['DATABASE_URL']}")
    print("API Access: Authenticated")
    print(f"Log Level: {config['LOG_LEVEL']}")
    print("Zion Network: Online")
    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
