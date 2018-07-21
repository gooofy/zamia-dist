#!/bin/sh

VERSION=1.0

rm -rf kenlm-${VERSION} kenlm-${VERSION}.tar.gz

cp -r kenlm kenlm-${VERSION}
tar cfvz kenlm-${VERSION}.tar.gz kenlm-${VERSION}

rm -rf kenlm-${VERSION}

rm -rf ~/rpmbuild
mkdir -p ~/rpmbuild/SOURCES
cp * ~/rpmbuild/SOURCES

rm kenlm-${VERSION}.tar.gz

rpmbuild -ba --clean kenlm.spec

