from app.init_logging import init_logging
from app.main import generate_message, generate_file


def main():
    print(generate_message())
    generate_file()


if __name__ == "__main__":
    init_logging()
    main()
