#!/bin/sh

VERSION=1.0.0

rm -rf py-xsb-${VERSION} py-xsb-${VERSION}.tar.gz

pushd py-xsb
make clean README.md
popd

cp -r py-xsb py-xsb-${VERSION}
tar cfvz py-xsb-${VERSION}.tar.gz py-xsb-${VERSION}

rm -rf py-xsb-${VERSION}

rm -rf ~/rpmbuild
mkdir -p ~/rpmbuild/SOURCES
cp * ~/rpmbuild/SOURCES

rpmbuild -ba --clean python-xsb.spec

rm -f py-xsb-${VERSION}.tar.gz

