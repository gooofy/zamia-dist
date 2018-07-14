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

rm -f py-picotts-${VERSION}.tar.gz

