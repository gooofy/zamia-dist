#!/bin/bash

RELEASE=r20190328
VERSION=20190328-1

rm -rf kaldi-chain-zamia-speech-de/opt
mkdir -p kaldi-chain-zamia-speech-de/opt/kaldi/model

cp -r kaldi-generic-de-tdnn_f-${RELEASE} kaldi-chain-zamia-speech-de/opt/kaldi/model/kaldi-generic-de-tdnn_f
cp -r kaldi-generic-de-tdnn_250-${RELEASE} kaldi-chain-zamia-speech-de/opt/kaldi/model/kaldi-generic-de-tdnn_250
cp -r kaldi-generic-de-tri2b_chain-${RELEASE} kaldi-chain-zamia-speech-de/opt/kaldi/model/kaldi-generic-de-tri2b_chain

# DEBIAN

mkdir -p kaldi-chain-zamia-speech-de/DEBIAN
sed "s/VERSION/${VERSION}/g" DEBIAN/control >kaldi-chain-zamia-speech-de/DEBIAN/control

# built .deb

echo "dpkg-deb..."

time fakeroot dpkg-deb --build kaldi-chain-zamia-speech-de

mv kaldi-chain-zamia-speech-de.deb kaldi-chain-zamia-speech-de_${VERSION}_armhf.deb

# run lintian on it

# lintian kaldi-chain-zamia-speech-de.deb | tee lr.txt

