import plistlib
import pathlib
import sys


class Optimization:
    def __init__(self, config_path: str):
        self.config_path = config_path

        self.base_config: dict = {}

    def run(self):
        path = pathlib.Path(__file__).parent / "OC-Kext-order"

        if not path.exists():
            print("Not found OC-Kext-order directory!")
            sys.exit(1)

        with open(path / "config.plist", "rb") as f:
            self.base_config = plistlib.load(f, fmt=plistlib.FMT_XML)
