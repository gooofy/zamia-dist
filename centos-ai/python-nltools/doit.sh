#!/bin/sh

VERSION=0.3.1

rm -rf py-nltools-${VERSION} py-nltools-${VERSION}.tar.gz

pushd py-nltools
make clean README.md
popd

cp -r py-nltools py-nltools-${VERSION}
tar cfvz py-nltools-${VERSION}.tar.gz py-nltools-${VERSION}

rm -rf py-nltools-${VERSION}

rm -rf ~/rpmbuild
mkdir -p ~/rpmbuild/SOURCES
cp * ~/rpmbuild/SOURCES

rpmbuild -ba --clean python-nltools.spec

rm -f py-nltools-${VERSION}.tar.gz

