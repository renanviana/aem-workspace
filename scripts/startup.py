import sys
import os
import zipfile
import json
import asyncio
import yaml

root = "/aem"

def setup_aem(executable):
    os.chdir(root)
    os.system(executable)

with open(f"{root}/config.yml", "r") as stream:
    config = yaml.safe_load(stream)
    if len(sys.argv) > 1:
        mode = sys.argv[1]
        executable = config[mode]["executable"]
        setup_aem(executable)
    else:
        print("ERROR: mode [author or publish] arg is required")
