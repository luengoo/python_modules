import sys


def handle_argv() -> None:
    print("=== Command Quest ===")
    i = 1
    if len(sys.argv) == 1:
        print("No arguments provided!")
    print(f"Program name: {sys.argv[0]}")
    if len(sys.argv) > 1:
        print(f"Arguments recieved: {len(sys.argv) - 1}")
        while i < len(sys.argv):
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1
    print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    handle_argv()
