import sys
import os
import zipfile
import json
import asyncio
import yaml

root = "/aem"
# protocol = "http"
# host = "localhost"
# auth = "admin:admin"

# async def await_startup(port):
#     print("Startup...")
#     success = check_replication_agent(port)
#     if not success:
#         await asyncio.sleep(30)
#         await await_startup(port)

# def check_replication_agent(port):
#     res = os.popen(f'curl -u {auth} {protocol}://{host}:{port}/etc/replication/agents.author/publish/jcr:content.queue.json?agent=publish').read()
#     print(res)
#     if res == "":
#         return False
#     else:
#         try:
#             data = json.loads(res)
#             return data["metaData"]["root"] == "queue"
#         except:
#             return False

def setup_aem(executable):
    os.chdir(root)
    os.system(executable)

with open(f"{root}/config.yml", "r") as stream:
    config = yaml.safe_load(stream)
    if len(sys.argv) > 1:
        mode = sys.argv[1]
        executable = config[mode]["executable"]
        if mode == "author":
            setup_aem(executable)
            
            # author_port = config["author"]["port"]
            # publish_port = config["publish"]["port"]
            # loop = asyncio.get_event_loop()
            # loop.run_until_complete(await_startup(author_port))
            # configure_replication_agent(author_port, publish_port)

            # os.chdir("/aem/packages")
            # if len(os.listdir()) > 0:
            #     for item in os.listdir():
            #         print(f"\nUploading package... {item}")
            #         upload_package(item, port)
            #         print(f"\nInstalling package... {item}")
            #         install_package(item, port)
                    # print(f"\nReplicating package... {item}")
                    # replicate_package(item, port)
        elif mode == "publish":
            setup_aem(executable)
        else:
            print("ERROR: mode [author or publish] incorrect")
    else:
        print("ERROR: mode [author or publish] arg is required")
