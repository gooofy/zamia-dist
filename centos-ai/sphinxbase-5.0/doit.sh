#!/bin/sh

VERSION=5.0

rm -rf sphinxbase-${VERSION} sphinxbase-${VERSION}.tar.gz

cp -r sphinxbase sphinxbase-${VERSION}
tar cfvz sphinxbase-${VERSION}.tar.gz sphinxbase-${VERSION}

rm -rf sphinxbase-${VERSION}

rm -rf ~/rpmbuild
mkdir -p ~/rpmbuild/SOURCES
cp * ~/rpmbuild/SOURCES

rm sphinxbase-${VERSION}.tar.gz

rpmbuild -ba --clean sphinxbase.spec

