#!/bin/sh

VERSION=0.1.2

rm -rf py-picotts-${VERSION} py-picotts-${VERSION}.tar.gz

pushd py-picotts
make clean README.md
popd

cp -r py-picotts py-picotts-${VERSION}
tar cfvz py-picotts-${VERSION}.tar.gz py-picotts-${VERSION}

rm -rf py-picotts-${VERSION}

rm -rf ~/rpmbuild
mkdir -p ~/rpmbuild/SOURCES
cp * ~/rpmbuild/SOURCES

rpmbuild -ba --clean python-picotts.spec

# cp ~/rpmbuild/RPMS/x86_64/*.rpm ~/repo/ai/centos/7/x86_64
# cp ~/rpmbuild/RPMS/noarch/*.rpm ~/repo/ai/centos/7/x86_64
# createrepo ~/repo/ai/centos/7/x86_64
# rsync --delete -avzP ~/repo/ai/ guenter@goofy.zamia.org:/var/www/html/repo-ai/
