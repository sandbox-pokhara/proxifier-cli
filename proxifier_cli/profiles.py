import os
import time

from proxifier_cli.process import close_proxifier
from proxifier_cli.process import start_proxifier

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


def create_profile(address, port, username, password, protocol="HTTPS"):
    with open(os.path.join(BASE_DIR, "profile.ppx")) as fp:
        profile = fp.read()
        return profile.format(
            protocol=protocol,
            password=password,
            username=username,
            port=port,
            address=address,
        )


def set_default_profile(address, port, username, password, protocol="HTTPS"):
    close_proxifier()
    time.sleep(5)
    default_file_path = os.path.join(
        os.path.expanduser("~"),
        "AppData",
        "Roaming",
        "Proxifier4",
        "Profiles",
        "Default.ppx",
    )
    os.makedirs(os.path.dirname(default_file_path), exist_ok=True)
    with open(default_file_path, "w") as fp:
        fp.write(create_profile(address, port, username, password, protocol))
    start_proxifier()
