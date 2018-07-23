#!/bin/sh

VERSION=0.1.0

rm -rf kaldi-adapt-lm-${VERSION} kaldi-adapt-lm-${VERSION}.tar.gz

cp -r kaldi-adapt-lm kaldi-adapt-lm-${VERSION}
tar cfvz kaldi-adapt-lm-${VERSION}.tar.gz kaldi-adapt-lm-${VERSION}

rm -rf kaldi-adapt-lm-${VERSION}

rm -rf ~/rpmbuild
mkdir -p ~/rpmbuild/SOURCES
cp * ~/rpmbuild/SOURCES

rpmbuild -ba --clean kaldi-adapt-lm.spec

rm -f kaldi-adapt-lm-${VERSION}.tar.gz

