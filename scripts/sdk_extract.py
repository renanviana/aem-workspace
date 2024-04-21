import zipfile
import os
import sys
import yaml

root = "/aem"
base = f"{root}/sdk"

def extract_sdk():
    os.chdir(base)
    if len(os.listdir()) > 0:
        for item in os.listdir():
            if ".zip" in item:
                with zipfile.ZipFile(f"./{item}", "r") as zip_ref:
                    zip_ref.extractall(base)
                    for item_extracted in os.listdir():
                        if item != item_extracted and ".jar" not in item_extracted:
                            os.system(f"rm -rf {item_extracted}")
                break

def move_rename_jar(port, mode):
    os.chdir(base)
    if len(os.listdir()) > 0:
        for item in os.listdir():
            if ".jar" in item:
                os.system(f"mv {item} {root}")
                os.chdir(root)
                os.system(f"mv {item} aem-{mode}-p{port}.jar")
                break

with open(f"{root}/config.yml", "r") as stream:
    config = yaml.safe_load(stream)
    if len(sys.argv) > 1:
        mode = sys.argv[1]
        port = config[mode]["port"]
        extract_sdk()
        move_rename_jar(port, mode)
    else:
        print("ERROR: mode [author or publish] arg is required")
