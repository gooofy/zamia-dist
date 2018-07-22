#!/bin/sh

VERSION=5.4

rm -rf kaldi-asr-${VERSION} kaldi-asr-${VERSION}.tar.gz

cp -r kaldi kaldi-asr-${VERSION}
tar cfvz kaldi-asr-${VERSION}.tar.gz kaldi-asr-${VERSION}
rm -rf kaldi-asr-${VERSION} 

rm -rf ~/rpmbuild
mkdir -p ~/rpmbuild/SOURCES
cp * ~/rpmbuild/SOURCES

rm kaldi-asr-${VERSION}.tar.gz

time rpmbuild -ba --clean kaldi-asr.spec

