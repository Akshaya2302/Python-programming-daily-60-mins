import os
import sys
import time
from typing import Generator


def typewriter_print(text: str, delay: float = 0.04) -> None:
    """Prints text to the terminal with a typewriter effect."""
    # ANSI escape codes for formatting (Bold Cyan)
    start_color = "\033[1;36m"
    end_color = "\033[0m"

    sys.stdout.write(start_color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(end_color + "\n")


def get_visitor_name() -> str:
    """Gets the username from environment or falls back to 'Guest'."""
    # Looks for standard environment variables, otherwise defaults
    return os.environ.get("USER") or os.environ.get("USERNAME") or "Guest"


def main() -> None:
    visitor = get_visitor_name()

    welcome_message = (
        f"👋 Hello, {visitor}!\n"
        "🚀 Welcome to my GitHub space.\n"
        "💻 Code, coffee, and constant learning happen here."
    )

    try:
        typewriter_print(welcome_message)
    except KeyboardInterrupt:
        # Gracefully handle Ctrl+C
        print("\n\033[1;31m🏃 Setup interrupted. See you around!\033[0m")


if __name__ == "__main__":
    main()