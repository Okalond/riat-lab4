"""Simple addition application for the CircleCI laboratory."""

import argparse


def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def main():
    parser = argparse.ArgumentParser(description="Add two numbers.")
    parser.add_argument("a", type=float, help="First number")
    parser.add_argument("b", type=float, help="Second number")
    args = parser.parse_args()
    print(f"{add(args.a, args.b):g}")


if __name__ == "__main__":
    main()
