import os
import subprocess

locations = [
    "C:\\Program Files (x86)\\Proxifier\\Proxifier.exe",
]


def start_proxifier():
    for l in locations:
        if os.path.isfile(l):
            subprocess.Popen(l)
            return True, None
    return False, "INSTALLATION_NOT_FOUND"


def close_proxifier():
    subprocess.call(
        "taskkill /f /IM proxifier.exe",
        stderr=subprocess.PIPE,
        stdout=subprocess.PIPE,
    )
