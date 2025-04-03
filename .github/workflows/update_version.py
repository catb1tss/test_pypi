import re
import subprocess
import requests
import json

def get_latest_version(package_name):
    url = f"https://test.pypi.org/rss/project/ra-catbit/releases.xml"
    response = requests.get(url)
    version = re.findall(r'\d+\.\d+\.\d+', response.text)[0]
    if not version:
        raise Exception("Failed parsing version")
    return version

def update_version(version):
    subprocess.run(["poetry", "version", version])
    subprocess.run(["poetry", "version", "patch"])

if __name__ == "__main__":
    update_version(get_latest_version("ra_catbit"))

