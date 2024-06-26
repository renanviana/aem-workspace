from fastapi import FastAPI, Response
import os

app = FastAPI()
protocol = "http"
auth = "admin:admin"
author_port = 4502
publish_port = 4503

@app.get("/packages/author/up-install")
def get_packages_author_up_install():
    return up_install("author")

@app.get("/packages/publish/up-install")
def get_packages_publish_up_install():
    return up_install("publish")

@app.get("/packages/author/upload")
def get_packages_author_upload():
    return upload("author")

@app.get("/packages/publish/upload")
def get_packages_publish_upload():
    return upload("publish")

@app.get("/packages/author/install")
def get_packages_author_install():
    return install("author")

@app.get("/packages/publish/install")
def get_packages_publish_install():
    return install("publish")

@app.get("/packages/author/replicate")
def get_packages_author_replicate():
    return replicate("author")

@app.get("/packages/publish/replicate")
def get_packages_publish_replicate():
    return replicate("publish")

@app.get("/config/replication")
def replication_config():
    res = os.popen(f'curl -u {auth} {protocol}://author:{author_port}/etc/replication/agents.author/publish -X POST -F "jcr:primaryType=cq:Page" -F "jcr:content/sling:resourceType=/libs/cq/replication/components/agent" -F "jcr:content/template=/libs/cq/replication/templates/agent" -F "jcr:content/enabled=true" -F "jcr:content/userId=" -F "jcr:content/transportUri=http://publish:{publish_port}/bin/receive?sling:authRequestLogin=1" -F "jcr:content/transportUser=admin" -F "jcr:content/transportPassword=admin"').read()
    return Response(content=res, media_type="application/xml")

def action(mode, results, rule):
    base = f"/src/{mode}/packages"
    os.chdir(base)
    if len(os.listdir()) > 0:
        for item in os.listdir():
            if ".zip" in item:
                if rule == "upload":
                    results["uploaded"][item] = upload_curl(f"{base}/{item}")
                if rule == "install":
                    results["installed"][item] = install_curl(item)
                if rule == "up-install":
                    results["uploaded"][item] = upload_curl(f"{base}/{item}")
                    results["installed"][item] = install_curl(item)
                if rule == "replicate":
                    results["replicated"][item] = replicate_curl(item)
    return results

def upload(mode):
    response = {}
    response["uploaded"] = {}
    return action(mode, response, "upload")

def install(mode):
    response = {}
    response["installed"] = {}
    return action(mode, response, "install")

def up_install(mode):
    response = {}
    response["uploaded"] = {}
    response["installed"] = {}
    return action(mode, response, "up-install")

def replicate(mode):
    response = {}
    response["replicated"] = {}
    return action(mode, response, "replicate")

def upload_curl(package_name):
    return os.popen(f'curl -u {auth} -F cmd=upload -F force=true -F package=@"{package_name}" {protocol}://author:{author_port}/crx/packmgr/service/.json').read()

def install_curl(package_name):
    return os.popen(f'curl -u {auth} -F cmd=install {protocol}://author:{author_port}/crx/packmgr/service/.json/etc/packages/my_packages/{package_name}').read()

def replicate_curl(package_name):
    return os.popen(f'curl -u {auth} -F cmd=replicate -X POST {protocol}://author:{author_port}/crx/packmgr/service/.json/etc/packages/my_packages/{package_name}').read()
