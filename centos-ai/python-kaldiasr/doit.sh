#!/bin/sh

VERSION=0.5.2

rm -rf py-kaldi-asr-${VERSION} py-kaldi-asr-${VERSION}.tar.gz

pushd py-kaldi-asr
make clean README.md
popd

cp -r py-kaldi-asr py-kaldi-asr-${VERSION}
tar cfvz py-kaldi-asr-${VERSION}.tar.gz py-kaldi-asr-${VERSION}

rm -rf py-kaldi-asr-${VERSION}

rm -rf ~/rpmbuild
mkdir -p ~/rpmbuild/SOURCES
cp * ~/rpmbuild/SOURCES

rpmbuild -ba --clean python-kaldiasr.spec

rm -f py-kaldi-asr-${VERSION}.tar.gz

