#!/bin/bash

RELEASE=r20190609
VERSION=20190609-1

rm -rf kaldi-chain-zamia-speech-en/opt
mkdir -p kaldi-chain-zamia-speech-en/opt/kaldi/model

cp -r kaldi-generic-en-tdnn_f-${RELEASE} kaldi-chain-zamia-speech-en/opt/kaldi/model/kaldi-generic-en-tdnn_f
cp -r kaldi-generic-en-tdnn_250-${RELEASE} kaldi-chain-zamia-speech-en/opt/kaldi/model/kaldi-generic-en-tdnn_250
cp -r kaldi-generic-en-tri2b_chain-${RELEASE} kaldi-chain-zamia-speech-en/opt/kaldi/model/kaldi-generic-en-tri2b_chain

# DEBIAN

mkdir -p kaldi-chain-zamia-speech-en/DEBIAN
sed "s/VERSION/${VERSION}/g" DEBIAN/control >kaldi-chain-zamia-speech-en/DEBIAN/control

# built .deb

echo "dpkg-deb..."

time fakeroot dpkg-deb --build kaldi-chain-zamia-speech-en

mv kaldi-chain-zamia-speech-en.deb kaldi-chain-zamia-speech-en_${VERSION}_armhf.deb

# run lintian on it

# lintian kaldi-chain-zamia-speech-en.deb | tee lr.txt

