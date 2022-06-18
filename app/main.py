import logging
import pathlib
from typing import Final
from faker import Faker

import ulid

faker = Faker()

ROOT_PATH: Final[pathlib.Path] = pathlib.Path(__file__).parents[1]
OUTPUT_PATH: Final[pathlib.Path] = ROOT_PATH.joinpath('output')


def generate_message():
    return f'Hello, {faker.unique.first_name()}'


def generate_file():
    temp_path = OUTPUT_PATH.joinpath(f'{ulid.new()}.txt')
    temp_path.write_text(generate_message())

    logging.info(f"File generated path: '{temp_path}'")