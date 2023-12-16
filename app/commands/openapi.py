import argparse
import json
from argparse import Namespace

from app.main import app


def get_args() -> Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output", required=True)

    return parser.parse_args()


def main() -> None:
    args = get_args()
    output = args.output

    openapi_data = app.openapi()

    with open(output, "w") as file:
        json.dump(openapi_data, file, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    main()
