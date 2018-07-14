#!/bin/sh

VERSION=5.0

rm -rf sphinxtrain-${VERSION} sphinxtrain-${VERSION}.tar.gz

cp -r sphinxtrain sphinxtrain-${VERSION}
tar cfvz sphinxtrain-${VERSION}.tar.gz sphinxtrain-${VERSION}
rm -rf sphinxtrain-${VERSION} 

rm -rf ~/rpmbuild
mkdir -p ~/rpmbuild/SOURCES
cp * ~/rpmbuild/SOURCES

rm sphinxtrain-${VERSION}.tar.gz

rpmbuild -ba --clean sphinxtrain.spec

