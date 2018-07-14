#!/bin/sh

VERSION=0.1.4

rm -rf py-marytts-${VERSION} py-marytts-${VERSION}.tar.gz

pushd py-marytts
make clean README.md
popd

cp -r py-marytts py-marytts-${VERSION}
tar cfvz py-marytts-${VERSION}.tar.gz py-marytts-${VERSION}

rm -rf py-marytts-${VERSION}

rm -rf ~/rpmbuild
mkdir -p ~/rpmbuild/SOURCES
cp * ~/rpmbuild/SOURCES

rpmbuild -ba --clean python-marytts.spec

rm -f py-marytts-${VERSION}.tar.gz

