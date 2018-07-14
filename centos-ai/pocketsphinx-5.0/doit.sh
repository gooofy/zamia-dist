#!/bin/sh

VERSION=5.0

rm -rf pocketsphinx-${VERSION} pocketsphinx-${VERSION}.tar.gz

cp -r pocketsphinx pocketsphinx-${VERSION}
tar cfvz pocketsphinx-${VERSION}.tar.gz pocketsphinx-${VERSION}
rm -rf pocketsphinx-${VERSION} 

rm -rf ~/rpmbuild
mkdir -p ~/rpmbuild/SOURCES
cp * ~/rpmbuild/SOURCES

rm pocketsphinx-${VERSION}.tar.gz

rpmbuild -ba --clean pocketsphinx.spec

