from fastapi import FastAPI, Response
import os

app = FastAPI()
protocol = "http"
auth = "admin:admin"
author_port = 4502
publish_port = 4503

@app.get("/packages/author/install")
def get_packages_author_install():
    return packages_install("author")

@app.get("/packages/publish/install")
def get_packages_publish_install():
    return packages_install("publish")

@app.get("/packages/author/replicate")
def get_packages_author_replicate():
    return packages_replication("author")

@app.get("/packages/publish/replicate")
def get_packages_publish_replicate():
    return packages_replication("publish")

@app.get("/config/replication")
def replication_config():
    res = os.popen(f'curl -u {auth} {protocol}://author:{author_port}/etc/replication/agents.author/publish -X POST -F "jcr:primaryType=cq:Page" -F "jcr:content/sling:resourceType=/libs/cq/replication/components/agent" -F "jcr:content/template=/libs/cq/replication/templates/agent" -F "jcr:content/enabled=true" -F "jcr:content/userId=" -F "jcr:content/transportUri=http://publish:{publish_port}/bin/receive?sling:authRequestLogin=1" -F "jcr:content/transportUser=admin" -F "jcr:content/transportPassword=admin"').read()
    return Response(content=res, media_type="application/xml")

def packages_install(mode):
    base = f"/src/{mode}/packages"
    os.chdir(base)
    response = {}
    response["uploaded"] = {}
    response["installed"] = {}
    if len(os.listdir()) > 0:
        for item in os.listdir():
            response["uploaded"][item] = upload_package(f"{base}/{item}")
            response["installed"][item] = install_package(item)
    return response

def packages_replication(mode):
    base = f"/src/{mode}/packages"
    os.chdir(base)
    response = {}
    response["replicated"] = {}
    if len(os.listdir()) > 0:
        for item in os.listdir():
            response["replicated"][item] = replicate_package(item)
    return response

def upload_package(package_name):
    return os.popen(f'curl -u {auth} -F cmd=upload -F force=true -F package=@"{package_name}" {protocol}://author:{author_port}/crx/packmgr/service/.json').read()

def install_package(package_name):
    return os.popen(f'curl -u {auth} -F cmd=install {protocol}://author:{author_port}/crx/packmgr/service/.json/etc/packages/my_packages/{package_name}').read()

def replicate_package(package_name):
    return os.popen(f'curl -u {auth} -F cmd=replicate -X POST {protocol}://author:{author_port}/crx/packmgr/service/.json/etc/packages/my_packages/{package_name}').read()
