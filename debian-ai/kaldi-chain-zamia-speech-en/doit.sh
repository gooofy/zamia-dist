#!/bin/bash

RELEASE=r20180702
VERSION=20180702-1

rm -rf kaldi-chain-zamia-speech-en/opt
mkdir -p kaldi-chain-zamia-speech-en/opt/kaldi/model

# kaldi-generic-en-tdnn_250-${RELEASE}.tar.xz  kaldi-generic-en-tdnn_sp-${RELEASE}.tar.xz

cp -r kaldi-generic-en-tdnn_sp-${RELEASE} kaldi-chain-zamia-speech-en/opt/kaldi/model/kaldi-generic-en-tdnn_sp
cp -r kaldi-generic-en-tdnn_250-${RELEASE} kaldi-chain-zamia-speech-en/opt/kaldi/model/kaldi-generic-en-tdnn_250

# DEBIAN

mkdir kaldi-chain-zamia-speech-en/DEBIAN
sed "s/VERSION/${VERSION}/g" DEBIAN/control >kaldi-chain-zamia-speech-en/DEBIAN/control

# built .deb

echo "dpkg-deb..."

time fakeroot dpkg-deb --build kaldi-chain-zamia-speech-en

mv kaldi-chain-zamia-speech-en.deb kaldi-chain-zamia-speech-en_${VERSION}_amd64.deb

# run lintian on it

# lintian kaldi-chain-zamia-speech-en.deb | tee lr.txt

