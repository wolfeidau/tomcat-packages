#!/usr/bin/env bash

# prepare fresh directories
rm -rf BUILD RPMS SRPMS tmp || true
mkdir -p BUILD RPMS SRPMS

# real action happens here
# rpmbuild -ba --define="_topdir $PWD" --define="_tmppath $PWD/tmp" SPECS/tomcat-base.spec
rpmbuild -bi --define="_topdir $PWD" --define="_tmppath $PWD/tmp" SPECS/tomcat-bamboo.spec
