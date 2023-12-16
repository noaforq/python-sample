import base64
import os


def main() -> None:
    service_account_key_base64 = os.environ["SERVICE_ACCOUNT_KEY"]

    service_account_key = base64.b64decode(service_account_key_base64)

    with open("./service-account-key.json", "w") as f:
        f.write(service_account_key.decode())


if __name__ == "__main__":
    main()
