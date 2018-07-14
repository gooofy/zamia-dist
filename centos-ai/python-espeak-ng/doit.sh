#!/bin/sh

VERSION=0.1.6

rm -rf py-espeak-ng-${VERSION} py-espeak-ng-${VERSION}.tar.gz

pushd py-espeak-ng
make clean README.md
popd

cp -r py-espeak-ng py-espeak-ng-${VERSION}
tar cfvz py-espeak-ng-${VERSION}.tar.gz py-espeak-ng-${VERSION}

rm -rf py-espeak-ng-${VERSION}

rm -rf ~/rpmbuild
mkdir -p ~/rpmbuild/SOURCES
cp * ~/rpmbuild/SOURCES

rpmbuild -ba --clean python-espeak-ng.spec

rm -f py-espeak-ng-${VERSION}.tar.gz

