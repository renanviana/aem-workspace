# Maple Bear AEM Author Container

## Startup

```bash
docker compose build
```

```bash
docker compose run --rm --service-ports -d 
```

Execute this command in root project 'aem-maple-bear-portal'

```bash
mvn clean install -PautoInstallBundle,autoInstallPackage -DskipTests && curl -u admin:admin http://localhost:4502/system/console/bundles/maple-bear.bundle -Faction=start
```

Access http://localhost:4502/system/console/bundles and start maple-bear.bundle

#!/bash

java -agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=0.0.0.0:5502 -Dadmin.password.file=passwordfile.properties -jar aem-author-p4502.jar -nointeractive

# curl -u admin:admin -F package=@"maple-bear-author-default-vars-6.1.1.zip" http://localhost:4502/crx/packmgr/service/.json/?cmd=upload && curl -u admin:admin -F cmd=install http://localhost:4502/crx/packmgr/service/.json/etc/packages/my_packages/maple-bear-author-default-vars-6.1.1.zip
# curl -u admin:admin -F package=@"maple-bear-publish-default-vars-6.1.1.zip" http://localhost:4503/crx/packmgr/service/.json/?cmd=upload && curl -u admin:admin -F cmd=install http://localhost:4503/crx/packmgr/service/.json/etc/packages/my_packages/maple-bear-publish-default-vars-6.1.1.zip
# curl -u admin:admin -F package=@"maple-bear-content-dev-9.4.7.zip" http://localhost:4502/crx/packmgr/service/.json/?cmd=upload && curl -u admin:admin -F cmd=install http://localhost:4502/crx/packmgr/service/.json/etc/packages/my_packages/maple-bear-content-dev-9.4.7.zip
# curl -u admin:admin http://localhost:4502/system/console/bundles/maple-bear.bundle -Faction=start


curl -u admin:admin -F package=@"maple-bear-publish-default-vars-6.1.1.zip" http://localhost:4503/crx/packmgr/service/.json/?cmd=upload && curl -u admin:admin -F cmd=install http://localhost:4503/crx/packmgr/service/.json/etc/packages/my_packages/maple-bear-publish-default-vars-6.1.1.zip