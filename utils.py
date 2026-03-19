import json


def load(file):
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
        return content

def xpath_file(file):
    with open(file, "r") as f:
        XPATHS = json.load(f)
        return XPATHS