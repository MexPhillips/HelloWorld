def main() -> str:
    name = input("What's your name? ")
    print(f"Hello, World!")
    return name


if __name__ == "__main__":
    print("Hello, world!")
    print(f"The person running this program is {main()}")